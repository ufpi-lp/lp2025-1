import struct
import os

# Configurações do arquivo binário
ARQUIVO_BIN = 'pessoas.bin'
# Formato fixo: CPF (11 bytes), Nome (50 bytes), Telefone (15 bytes)
# O 's' indica string de bytes. O número à esquerda define o tamanho exato.
FORMATO = '11s50s15s'
TAMANHO_REGISTRO = struct.calcsize(FORMATO)  # 76 bytes por registro

def decodificar_campo(b):
    """Remove bytes nulos de preenchimento e converte para string."""
    return b.decode('utf-8').strip('\x00').strip()

def ler_dados():
    cpf = input("Digite o CPF (11 dígitos): ").strip()
    nome = input("Digite o nome: ").strip()
    telefone = input("Digite o telefone: ").strip()
    return cpf, nome, telefone

def cadastrar_pessoa():
    cpf, nome, telefone = ler_dados()
    
    # Validação básica para evitar estouro no struct
    if len(cpf) > 11 or len(nome) > 50 or len(telefone) > 15:
        print("Erro: Um ou mais campos excedem o limite de caracteres permitido.")
        return

    # struct.pack() transforma os dados em binário no formato definido
    dados_bin = struct.pack(FORMATO, cpf.encode('utf-8'), nome.encode('utf-8'), telefone.encode('utf-8'))
    
    # Abre em modo append binário e grava diretamente
    with open(ARQUIVO_BIN, 'ab') as arquivo:
        arquivo.write(dados_bin)
    print("Pessoa cadastrada com sucesso no arquivo binário!")

def listar_pessoas():
    if not os.path.exists(ARQUIVO_BIN):
        print("Arquivo não encontrado. Cadastre alguém primeiro.")
        return

    with open(ARQUIVO_BIN, 'rb') as arquivo:
        # file.seek(offset, whence) -> posiciona no início do arquivo (whence=0)
        arquivo.seek(0, 0)
        
        idx = 0
        while True:
            # Pula para o início do registro atual
            arquivo.seek(idx * TAMANHO_REGISTRO, 0)
            
            # file.read() lê exatamente o tamanho de um registro
            bloco = arquivo.read(TAMANHO_REGISTRO)
            if len(bloco) < TAMANHO_REGISTRO:
                break  # Fim do arquivo ou dados incompletos
                
            # struct.unpack() converte os bytes de volta para os campos
            cpf, nome, telefone = struct.unpack(FORMATO, bloco)
            print(f"[{idx}] CPF: {decodificar_campo(cpf)} | Nome: {decodificar_campo(nome)} | Tel: {decodificar_campo(telefone)}")
            idx += 1
            
    if idx == 0:
        print("Nenhum registro encontrado.")

def buscar_por_cpf():
    cpf_busca = input("Digite o CPF para buscar: ").strip()
    if not os.path.exists(ARQUIVO_BIN):
        print("Arquivo não encontrado.")
        return

    with open(ARQUIVO_BIN, 'rb') as arquivo:
        arquivo.seek(0, 0)
        posicao = 0
        encontrado = False
        
        while True:
            arquivo.seek(posicao, 0)
            bloco = arquivo.read(TAMANHO_REGISTRO)
            if len(bloco) < TAMANHO_REGISTRO:
                break
                
            cpf, nome, telefone = struct.unpack(FORMATO, bloco)
            if decodificar_campo(cpf) == cpf_busca:
                print(f"Encontrado na posição {posicao // TAMANHO_REGISTRO}: "
                      f"CPF: {decodificar_campo(cpf)} | Nome: {decodificar_campo(nome)} | Tel: {decodificar_campo(telefone)}")
                encontrado = True
                break
            posicao += TAMANHO_REGISTRO
            
    if not encontrado:
        print("CPF não encontrado no arquivo.")

def exibir_menu():
    print("\n" + "="*40)
    print("CADASTRO EM ARQUIVO BINÁRIO")
    print("="*40)
    print("1. Cadastrar pessoa")
    print("2. Listar todas as pessoas")
    print("3. Buscar por CPF")
    print("4. Sair")

def main():
    print("💡 Dados são gravados diretamente no arquivo .bin. Não é necessário 'Salvar' ou 'Carregar'.")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            buscar_por_cpf()
        elif opcao == "4":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
