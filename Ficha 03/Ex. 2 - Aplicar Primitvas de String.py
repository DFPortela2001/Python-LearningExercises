'''
Dada a seguinte string:

str1 = 'a amada lisboa e o rio tejo belo encantam toda a gente'
Aplique as primitivas da classe string (index, count, in, seletor [:], len, replace,
etc.) para apresentar os seguintes resultados:
'''

str1 = 'a amada lisboa e o rio tejo belo encantam toda a gente'

# a) Imprima os carateres a partir da 1a posição da letra 'b':
print("a) " + str1[str1.index('b'):])

# b) Imprima os carateres desde o início até à 1a posição da letra 'b':
print("b) " + str1[:str1.index('b')])

# c) Imprima a posição (índice) da 1a letra ‘a’:
print("c) " + str(str1.index('a')))

# d) Imprima a quantidade de letras ‘a’ contidas nela:
print("d) " + str(str1.count('a')))

# e) Imprima o comprimento da string (número total de carateres):
print("e) " + str(len(str1)))

# f) Substitua todos os espaços por ‘#’:
print("f) " + str1.replace(' ', '#'))

# g) Teste se a string contém a palavra 'tejo':
print("g) " + str('tejo' in str1))