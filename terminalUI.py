import requests

import os
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv('HOST')  # URL do servidor Flask
SERVER_PORT = os.getenv('PORT')
def ask_server(prompt: str) -> str:
    """
    Envie um prompt para o servidor.
    """
    data = {"prompt": prompt}
   
    try:
        response = requests.post(SERVER_URL+":"+SERVER_PORT, json=data)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar ao servidor: {e}"

def main():
    while True:
    
        prompt = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if prompt.lower() == "sair":
            print("Encerrando o cliente...")
            break

        print("\nEnviando pergunta ao servidor...")
        result = ask_server(prompt)

        if isinstance(result, dict):
            print("\nResposta do servidor:")
            print(f"Resposta: {result.get('response')}")
            if "command_output" in result:
                print(f"Saída do comando: {result.get('command_output')}")
        else:
            print(result)  

if __name__ == "__main__":
    main()