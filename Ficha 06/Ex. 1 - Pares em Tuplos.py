'''
Escreva em Python um programa que recebe do teclado um tuplo de inteiros e
devolve um tuplo contendo apenas os algarismos pares.
Exemplo de utilização:
Insira um tuplo de inteiros positivos: 1,6,7,99,56
Algarismos pares: (6, 56)
'''

def filtrar_pares(tuplo):
    pares = tuple(x for x in tuplo if x % 2 == 0)
    return pares

tuplo_str = input("Insira um tuplo de inteiros positivos: ")
tuplo = tuple(map(int, tuplo_str.split(',')))
pares = filtrar_pares(tuplo)
print("Algarismos pares:", pares)
