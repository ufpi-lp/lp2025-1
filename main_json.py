import json

# Dicionário para armazenar pessoas
pessoas = {}
ARQUIVO_JSON = "pessoas.json"

def ler_dados():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    return cpf, nome, telefone

def cadastrar_pessoa():
    cpf, nome, telefone = ler_dados()
    pessoas[cpf] = {"nome": nome, "telefone": telefone}
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    for cpf, dados in pessoas.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Telefone: {dados['telefone']}")

def salvar_dados():
    # json.dump converte o dicionário Python para JSON e grava no arquivo
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(pessoas, arquivo, indent=4, ensure_ascii=False)
    print("Dados salvos em 'pessoas.json'!")

def carregar_dados():
    global pessoas
    try:
        # json.load lê o arquivo JSON e converte diretamente para um dicionário Python
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            pessoas = json.load(arquivo)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Um novo será criado ao salvar.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Formato inválido ou corrompido.")
        pessoas = {}

def exibir_menu():
    print("\n1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Salvar dados")
    print("4. Sair")

def main():
    print("Protótipo de cadastro (dados mantidos em arquivo .json)")
    carregar_dados()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            salvar_dados()
        elif opcao == "4":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
