def tratar_linha(linha):
    return linha.strip().capitalize()

def criar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('Esta eh a primeira linha\n')
    print(f"> Arquivo '{nome_arquivo}' criado com sucesso!")

def acrescentar_linhas(nome_arquivo):
    print("> Digite as linhas a serem adicionadas (digite '0' para encerrar):")
    with open(nome_arquivo, 'a') as arquivo:
        while True:
            linha = input('> ')
            if linha == '0':
                break
            arquivo.write(tratar_linha(linha) + '\n')
    print("> Linhas adicionadas com sucesso!")

def mostrar_conteudo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print('> Conteúdo do arquivo:')
        print(conteudo)
    except FileNotFoundError:
        print(f"> Arquivo '{nome_arquivo}' não encontrado. Crie-o primeiro com a opção 1.")

def menu():
    nome_arquivo = 'arquivo.txt'
    while True:
        print("\nMENU")
        print("1. Criar um arquivo")
        print("2. Acrescentar linhas ao arquivo")
        print("3. Mostrar o conteúdo do arquivo")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            nome_input = input("Informe o nome do arquivo [arquivo.txt]: ").strip()
            if nome_input:
                nome_arquivo = nome_input
            criar_arquivo(nome_arquivo)

        elif opcao == '2':
            acrescentar_linhas(nome_arquivo)

        elif opcao == '3':
            mostrar_conteudo(nome_arquivo)

        elif opcao == '0':
            print("> Encerrando o programa...")
            break

        else:
            print("> Opção inválida. Tente novamente.")

# Execução do menu
menu()