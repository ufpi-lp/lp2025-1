# Dicionário para armazenar pessoas (apenas em memória)
pessoas = {}

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

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Sair")

def main():
    print("Protótipo de cadastro (dados mantidos apenas em memória)")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("Programa encerrado. Os dados não foram salvos em disco.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
