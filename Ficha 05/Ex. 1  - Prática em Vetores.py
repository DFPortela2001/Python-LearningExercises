'''
Escreva um programa que leia um conjunto de cinco valores do tipo float
digitados, carregando-os, um a um, num vetor unidimensional de cinco
elementos e, que, seguidamente, passe-o (o vetor) a uma função.

Esta, por sua vez, deve calcular e devolver ao programa chamante a quantidade
(número de ocorrências) de valores acima de 20.00.

Por sua vez, o programa chamante deve imprimir este resultado (o valor que
foi devolvido).
'''

def valores(vetor):
    count = 0
    soma = 0.0
    acima_20 = []
    for valor in vetor:
        if valor > 20.00:
            count += 1
            soma += valor
            acima_20.append(valor)
    return count, soma, acima_20

def main():
    vetor = []
    for i in range(5):
        valor = float(input(f"Escreva o {i+1}º valor (de 5): "))
        vetor.append(valor)
    
    count, soma, acima_20 = valores(vetor)
    print(f"Existem: {count} valores acima de 20.00")
    print(f"Os valores acima de 20.00 são: {acima_20}")
    print(f"A sua Soma é: {soma}")

if __name__ == "__main__":
    main()
