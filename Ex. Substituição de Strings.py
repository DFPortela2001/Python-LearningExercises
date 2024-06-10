'''
Crie um programa que faça pesquisas numa determinada string base com o
objetivo de substituir determinadas substrings por outras.
Exemplo do resultado que se pretende de uma execução tipo do programa:
Digite uma frase:

a ana e o aniceto foram ao cinema anadia

Digite uma substring a ser substituída:
ana
Digite uma substring de substituição:
lisboa

Resposta:

a lisboa e o aniceto foram ao cinema lisboadia

Nota:
a. O conteúdo da string base deve ficar efetivamente alterado. Ou seja,
imprimindo a string base, após as substituições, ela deve conter as
alterações que foram efetuadas.
b. Se a substring a ser substituída não for encontrada, o programa deve
informar ao utilizador dessa situação.
'''
def substitui_substring():
    global frase
    frase = input("Digite uma frase: ")
    substituicao = input("Digite uma palavra a ser substituida: ")
    substring = input("Digite a nova palavra: ")
    if substituicao not in frase:
        print("A palavra a ser substituída não foi encontrada na frase. \n")
        return
    else:
        frase = frase.replace(substituicao, substring)
        print(frase)
    

substitui_substring()
print('Conteúdo efetivo: ',frase)
