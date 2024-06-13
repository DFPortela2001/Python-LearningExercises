'''
Desenvolva um programa que aplique as técnicas de programação inerentes aos
Ficheiros de Texto para a obtenção de um determinado conjunto de cálculos
estatísticos a partir de um ficheiro de texto livre, criado por si, sob a forma de
ocorrências/quantidades, conforme abaixo descrito:

a) De cada vogal (frequência discriminada das ocorrências de cada vogal).
b) Das consoantes (totalidade das consoantes)
c) Das palavras (totalidade das palavras)
d) Das linhas

Inclua exceções e tratamento de quaisquer anomalias que possam ocorrer com
a abertura do ficheiro.
'''
import string

def contar_vogais(frase):
    contagem_vogais = {vogal: 0 for vogal in "aeiou"}
    for char in frase.lower():
        if char in contagem_vogais:
            contagem_vogais[char] += 1
    return contagem_vogais

def contar_consoantes(frase):
    total_consoantes = 0
    for char in frase.lower():
        if char in string.ascii_lowercase and char not in "aeiouáéíóúãẽĩõũàèìòùâêîôûäëïöüÁÉÍÓÚÃẼĨÕŨÀÈÌÒÙÂÊÎÔÛÄËÏÖÜ":
            total_consoantes += 1
    return total_consoantes

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def contar_linhas(nome_ficheiro):
    total_linhas = 0
    try:
        ficheiro = open(nome_ficheiro, 'r', encoding='utf-8')
        for _ in ficheiro:
            total_linhas += 1
        ficheiro.close()
    except FileNotFoundError:
        print(f"O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return -1
    except IOError:
        print(f"Ocorreu um erro ao tentar ler o ficheiro '{nome_ficheiro}'.")
        return -1
    return total_linhas

def leitura_ficheiros(nome_ficheiro):
    contagem_vogais = {vogal: 0 for vogal in "aeiou"}
    total_consoantes = 0
    total_palavras = 0
    total_linhas = 0
    
    try:
        ficheiro = open(nome_ficheiro, 'r', encoding='utf-8')
        for linha in ficheiro:
            total_linhas += 1
            palavras = linha.split()
            total_palavras += len(palavras)
            
            for palavra in palavras:
                for char in palavra.lower():
                    if char in contagem_vogais:
                        contagem_vogais[char] += 1
                    elif char in string.ascii_lowercase and char not in "aeiou":
                        total_consoantes += 1
        ficheiro.close()
    except FileNotFoundError:
        print(f"O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return
    except IOError:
        print(f"Ocorreu um erro ao tentar ler o ficheiro '{nome_ficheiro}'.")
        return

    print("Frequência de cada vogal:")
    for vogal, contagem in contagem_vogais.items():
        print(f"{vogal}: {contagem}")
    
    print(f"\nTotal de consoantes: {total_consoantes}")
    print(f"Total de palavras: {total_palavras}")
    print(f"Total de linhas: {total_linhas}")


nome_ficheiro = input("Escreva o nome do ficheiro (com a extensão): ")
leitura_ficheiros(nome_ficheiro)
