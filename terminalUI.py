import requests

import os
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv('HOST')  # URL do servidor Flask
SERVER_PORT = os.getenv('PORT')
def ask_server(prompt: str) -> str:
    """
    Send a prompt to the server.
    """
    data = {"prompt": prompt}
   
    try:
        url = "http://"+SERVER_URL+":"+SERVER_PORT+"/ask"
        response = requests.post(url, json=data)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Fail to conect to the server: {e}"

def main():
    while True:
    
        prompt = input("\n Type your prompt (press ctrl + c or type 'quit'): ").strip()
        if prompt.lower() == "quit":
            print("Goodbye!...")
            break

        print("\n Sending Prompt to the server...")
        result = ask_server(prompt)

        if isinstance(result, dict):
            print("\n Server callback:")
            print(f"Response: {result.get('response')}")
            if "command_output" in result:
                print(f"Command return: {result.get('command_output')}")
        else:
            print(result)  

if __name__ == "__main__":
    main()