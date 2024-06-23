'''
Considere o tuplo numeros = (10,15,3,6,99,45,63,30,344,22,4,25,10).
Escreva um programa em Python que implementa as seguintes instruções:
'''

def main():
    numeros = (10, 15, 3, 6, 99, 45, 63, 30, 344, 22, 4, 25, 10)

    # a) Comprimento do tuplo
    comprimento = len(numeros)
    print("Comprimento do tuplo:", comprimento)

    # b) Máximo e mínimo do tuplo
    max_valor = max(numeros)
    min_valor = min(numeros)
    print("Máximo do tuplo:", max_valor)
    print("Mínimo do tuplo:", min_valor)

    # c) Cria um novo tuplo numeros3 juntando numeros com numeros2
    numeros2 = (21, 53, 23, 54, 22, 2, 1, 13)
    numeros3 = numeros + numeros2
    print("Novo tuplo numeros3:", numeros3)

    # d) Imprime os elementos de índice ímpar
    elementos_impares = numeros[1::2]
    print("Elementos de índice ímpar:", elementos_impares)

    # e) Imprime os elementos que são múltiplos de 5
    multiplos_de_5 = tuple(x for x in numeros if x % 5 == 0)
    print("Elementos múltiplos de 5:", multiplos_de_5)

if __name__ == "__main__":
    main()
