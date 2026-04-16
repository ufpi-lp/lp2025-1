import struct
import os

# Configurações do arquivo binário
ARQUIVO = 'pessoas_variavel.bin'

# Formato do cabeçalho: '<III' significa 3 inteiros sem sinal (4 bytes cada) em little-endian.
# Armazena: tamanho_do_cpf, tamanho_do_nome, tamanho_do_telefone (em bytes)
HEADER_FORMAT = '<III'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)  # 12 bytes

def ler_dados():
    cpf = input("Digite o CPF: ").strip()
    nome = input("Digite o nome: ").strip()
    telefone = input("Digite o telefone: ").strip()
    return cpf, nome, telefone

def cadastrar_pessoa():
    cpf, nome, telefone = ler_dados()
    
    # Converte strings para bytes (UTF-8)
    cpf_b, nome_b, tel_b = cpf.encode('utf-8'), nome.encode('utf-8'), telefone.encode('utf-8')
    
    # struct.pack() cria o cabeçalho binário com os tamanhos reais dos campos
    header = struct.pack(HEADER_FORMAT, len(cpf_b), len(nome_b), len(tel_b))
    
    # Grava cabeçalho + dados diretamente no arquivo
    with open(ARQUIVO, 'ab') as f:
        f.write(header)
        f.write(cpf_b)
        f.write(nome_b)
        f.write(tel_b)
    print("✅ Pessoa cadastrada com sucesso!")

def listar_pessoas():
    if not os.path.exists(ARQUIVO):
        print("⚠️ Arquivo não encontrado. Cadastre alguém primeiro.")
        return

    with open(ARQUIVO, 'rb') as f:
        pos = 0  # Posição atual no arquivo
        idx = 0  # Índice do registro
        
        print("\n📋 LISTA DE PESSOAS:")
        print("-" * 55)
        
        while True:
            # file.seek(offset, whence): posiciona o ponteiro no início do registro
            # whence=0 indica deslocamento a partir do início do arquivo
            f.seek(pos, 0)
            
            # Lê apenas o cabeçalho (12 bytes)
            header_data = f.read(HEADER_SIZE)
            if len(header_data) < HEADER_SIZE:
                break  # Fim do arquivo ou registro corrompido
                
            # struct.unpack() extrai os tamanhos reais dos campos
            len_cpf, len_nome, len_tel = struct.unpack(HEADER_FORMAT, header_data)
            total_dados = len_cpf + len_nome + len_tel
            
            # file.read() lê exatamente a quantidade de bytes informada no cabeçalho
            dados = f.read(total_dados)
            if len(dados) < total_dados:
                break  # Dados truncados
                
            # Separa os bytes conforme os tamanhos lidos
            cpf = dados[:len_cpf].decode('utf-8')
            nome = dados[len_cpf:len_cpf+len_nome].decode('utf-8')
            telefone = dados[len_cpf+len_nome:].decode('utf-8')
            
            print(f"[{idx}] CPF: {cpf:<14} | Nome: {nome:<20} | Tel: {telefone}")
            
            # Atualiza a posição para o próximo registro (cabeçalho + dados)
            pos = f.tell()
            idx += 1
            
        print("-" * 55)
        if idx == 0:
            print("(Nenhum registro encontrado)")

def buscar_por_cpf():
    cpf_busca = input("Digite o CPF para buscar: ").strip()
    if not os.path.exists(ARQUIVO):
        print("⚠️ Arquivo não encontrado.")
        return

    with open(ARQUIVO, 'rb') as f:
        pos = 0
        while True:
            f.seek(pos, 0)
            header_data = f.read(HEADER_SIZE)
            if len(header_data) < HEADER_SIZE:
                break
                
            len_cpf, len_nome, len_tel = struct.unpack(HEADER_FORMAT, header_data)
            dados = f.read(len_cpf + len_nome + len_tel)
            if len(dados) < len_cpf:
                break
                
            cpf = dados[:len_cpf].decode('utf-8')
            
            if cpf == cpf_busca:
                nome = dados[len_cpf:len_cpf+len_nome].decode('utf-8')
                telefone = dados[len_cpf+len_nome:].decode('utf-8')
                
                # Demonstra seek explícito para voltar ao início do registro encontrado
                f.seek(pos, 0)
                print(f"\n✅ Encontrado no deslocamento (offset) {pos} bytes:")
                print(f"   CPF: {cpf}")
                print(f"   Nome: {nome}")
                print(f"   Telefone: {telefone}")
                return
                
            pos = f.tell()  # Avança para o próximo registro
            
    print("❌ CPF não encontrado no arquivo.")

def exibir_menu():
    print("\n" + "="*40)
    print("📦 CADASTRO BINÁRIO (CAMPOS VARIÁVEIS)")
    print("="*40)
    print("1. Cadastrar pessoa")
    print("2. Listar todas as pessoas")
    print("3. Buscar por CPF")
    print("4. Sair")

def main():
    print("💡 Dados são gravados diretamente no arquivo .bin com cabeçalhos de registro.")
    print("   Não há dicionário em memória. Cada leitura/escrita é direta no disco.")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            buscar_por_cpf()
        elif opcao == "4":
            print("👋 Programa encerrado. Até mais!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
