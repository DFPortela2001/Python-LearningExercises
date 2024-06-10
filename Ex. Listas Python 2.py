'''
Considere a lista numeros = [1,5,3,6,22,45,63,30,344,22,12,25,10].
Escreva um programa em Python que implementa as seguintes instruções:
a) Inverta a lista
b) Ordene a lista por ordem crescente.
c) Imprima os últimos três elementos da lista.
'''
numeros = [1,5,3,6,22,45,63,30,]
print("Lista original:", numeros)
# a) Inverta a lista
numeros.reverse()
print("Lista invertida:", numeros)
# b) Ordene a lista por ordem crescente.
numeros.sort()
print("Lista ordenada:", numeros)
# c) Imprima os últimos três elementos da lista.
print("Últimos três elementos:", numeros[-3:])
