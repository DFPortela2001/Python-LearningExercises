'''
Crie uma lista, chamada lista1, com os seguintes valores: 'Iva', 25, 'Rui', 19,
'Rato', 'abc', 33
'''

lista1 = ['Iva',25,'Rui',19,'Rato','abc',33]
#A Imprimir a lista toda:
print(lista1)
#B Imprima os elementos de 2 a 4 (inclusive)
print(lista1[2:5])
#C Imprima os elementos do início até ao elemento 3 (exclusive)
print(lista1[:3])
#D Imprima os elementos de 3 até ao fim da lista
print(lista1[3:])
lista2 = ['Pizza', 420]
#E Crie uma nova lista, com valores à sua escolha, chamada lista2, e junte-a à lista1, criando assim uma nova lista.

#lista1.extend(lista2)
lista3 = lista1+lista2
print(lista1)