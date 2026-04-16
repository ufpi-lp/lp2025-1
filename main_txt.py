# Dicionário para armazenar pessoas
pessoas = {}

# Funções
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
    for cpf, dados in pessoas.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Telefone: {dados['telefone']}")

def salvar_dados():
    with open("pessoas.txt", "w") as arquivo:
        for cpf, dados in pessoas.items():
            linha = f"{cpf},{dados['nome']},{dados['telefone']}\n"
            arquivo.write(linha)
    print("Dados salvos em 'pessoas.txt'!")

def carregar_dados():
    try:
        with open("pessoas.txt", "r") as arquivo:
            for linha in arquivo:
                cpf, nome, telefone = linha.strip().split(",")
                pessoas[cpf] = {"nome": nome, "telefone": telefone}
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Um novo será criado ao salvar.")

def exibir_menu():
    print("1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Salvar dados")
    print("4. Sair")

# Menu principal
def main():
    print("Protótipo de cadastro (dados mantidos em arquivo .txt)")
    carregar_dados()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
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
