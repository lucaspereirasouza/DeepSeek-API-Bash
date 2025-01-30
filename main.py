from flask import Flask, request, jsonify
import requests
import subprocess
import shlex

import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


app = Flask(__name__)

def ask_deepseek(prompt):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100 
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("response", "Error 200: Response Not found.")
    else:
        return f"Erro na API: {response.status_code} - {response.text}"

def execute_bash_command(command):
    try:
        parsed_command = shlex.split(command, posix=True)
        if not parsed_command:
            return "Erro: Empty or Invalid command."

        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"
    except Exception as e:
        return f"man, what are you doing? UNEXPECTED ERROR: {str(e)}"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt")
    args = data.get("args", {})  

    if not prompt:
        return jsonify({"error": "It is necessary to ask something in the field."}), 400

    if args:
        for key, value in args.items():
            placeholder = f"{{{key}}}"
            prompt = prompt.replace(placeholder, str(value))

    response = ask_deepseek(prompt)

    if "bash" in response.lower() or "&&" in response or ";" in response:
        command_output = execute_bash_command(response)
        return jsonify({"response": response, "command_output": command_output})
    else:
        return jsonify({"response": response})

if __name__ == "__main__":
    print(f"Server running in http://{HOST}:{PORT}")
    app.run(host=HOST, port=PORT)