'''
Crie uma lista de 10 elementos, contendo dados à sua escolha, não digitados, mas que
sejam de diferentes tipos, tais como inteiros, floats e strings.
A partir desta lista através e através da aplicação do comando type crie três listas, cada
uma para exclusivamente um diferente tipo de dados.
Por exemplo:
Criada a sua lista:
lista1 = ["gato", 33, "pardal", 23.7, "macaco", "lia"", 45, 18.35, "zebra", "rato"]
As seguintes três listas devem ser criadas pelo programa:
lista_strs = ['gato', 'pardal', 'macaco', "lia", "zebra", "rato"]
lista_ints = [33, 45]
lista_floats = [23.7, 18.35]
'''

lista1 = ['gato',69,'pardal',23.5,'cão','daniel',23,19.99,"zebra"]
lista_strs = []
lista_ints = []
lista_floats = []
for elemento in lista1:
    if type(elemento) == str:
        lista_strs.append(elemento)
    elif type(elemento) == int:
        lista_ints.append(elemento)
    elif type(elemento) == float:
        lista_floats.append(elemento)
print("Lista original: ",lista1)
print("Lista de strings:", lista_strs)
print("Lista de inteiros:", lista_ints)
print("Lista de floats:", lista_floats)
