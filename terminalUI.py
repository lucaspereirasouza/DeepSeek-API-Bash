import requests

# Configurações
SERVER_URL = "https://127.0.0.0:5000/ask"  # URL do servidor Flask

def ask_server(prompt: str, args: dict = None) -> str:
    """
    Envia uma pergunta para o servidor e retorna a resposta.
    """
    data = {"prompt": prompt}
    if args:
        data["args"] = args

    try:
        response = requests.post(SERVER_URL, json=data)
        response.raise_for_status()  # Verifica se houve erro na requisição
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar ao servidor: {e}"

def main():
    while True:
        # Solicita a pergunta ao usuário
        prompt = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if prompt.lower() == "sair":
            print("Encerrando o cliente...")
            break

        # Solicita argumentos, se necessário
        args = {}
        while True:
            arg_key = input("Digite o nome de um argumento (ou deixe em branco para continuar): ").strip()
            if not arg_key:
                break
            arg_value = input(f"Digite o valor para '{arg_key}': ").strip()
            args[arg_key] = arg_value

        # Envia a pergunta ao servidor
        print("\nEnviando pergunta ao servidor...")
        result = ask_server(prompt, args if args else None)

        # Exibe a resposta
        if isinstance(result, dict):
            print("\nResposta do servidor:")
            print(f"Resposta: {result.get('response')}")
            if "command_output" in result:
                print(f"Saída do comando: {result.get('command_output')}")
        else:
            print(result)  # Exibe mensagens de erro

if __name__ == "__main__":
    main()