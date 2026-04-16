import csv

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
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    for cpf, dados in pessoas.items():
        print(f"CPF: {cpf}, Nome: {dados['nome']}, Telefone: {dados['telefone']}")

def salvar_dados():
    # newline="" é obrigatório no Python 3 para evitar linhas em branco extras no Windows
    with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        # Cabeçalho opcional (recomendado para organização)
        escritor.writerow(["CPF", "Nome", "Telefone"])
        for cpf, dados in pessoas.items():
            escritor.writerow([cpf, dados["nome"], dados["telefone"]])
    print("Dados salvos em 'pessoas.csv'!")

def carregar_dados():
    try:
        with open("pessoas.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                # Pula a linha de cabeçalho se existir
                if linha and linha[0] == "CPF":
                    continue
                # Validação simples para evitar linhas vazias ou malformadas
                if len(linha) == 3:
                    cpf, nome, telefone = linha
                    pessoas[cpf] = {"nome": nome, "telefone": telefone}
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Um novo será criado ao salvar.")

def exibir_menu():
    print("\n1. Cadastrar pessoa")
    print("2. Listar pessoas")
    print("3. Salvar dados")
    print("4. Sair")

# Menu principal
def main():
    print("Protótipo de cadastro (dados mantidos em arquivo .csv)")
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
