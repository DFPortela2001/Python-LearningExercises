'''
Escreva um programa que faça a leitura de um ficheiro de texto e que,
seguidamente, volte a gravar o mesmo ficheiro, mas somente contendo as
palavras únicas (sem as palavras repetidas).
Inclua exceções e tratamento de quaisquer anomalias que possam ocorrer com
a abertura do ficheiro.
'''


def ler_ficheiro(nome_ficheiro):
    try:
        ficheiro = open(nome_ficheiro, 'r', encoding='utf-8')
        conteudo = ficheiro.read()
        ficheiro.close()
        return conteudo
    except FileNotFoundError:
        print(f"O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return None
    except IOError:
        print(f"Ocorreu um erro ao tentar ler o ficheiro '{nome_ficheiro}'.")
        return None

def escrever_ficheiro(nome_ficheiro, conteudo):
    try:
        ficheiro = open(nome_ficheiro, 'w', encoding='utf-8')
        ficheiro.write(conteudo)
        ficheiro.close()
    except IOError:
        print(f"Ocorreu um erro ao tentar escrever no ficheiro '{nome_ficheiro}'.")

def processar_ficheiro(nome_ficheiro):
    conteudo = ler_ficheiro(nome_ficheiro)
    if conteudo is None:
        return

    palavras = conteudo.split()
    palavras_unicas = set(palavras) 
    conteudo_unico = ' '.join(palavras_unicas)

    escrever_ficheiro(nome_ficheiro, conteudo_unico)
    print(f"O ficheiro '{nome_ficheiro}' foi atualizado com palavras únicas.")

def main():
    nome_ficheiro = input("Escreva o nome do ficheiro (com a extensão): ")
    processar_ficheiro(nome_ficheiro)

if __name__ == "__main__":
    main()
