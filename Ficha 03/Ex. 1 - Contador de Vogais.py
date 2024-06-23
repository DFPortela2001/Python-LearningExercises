'''
Escreva um programa que leia uma string digitada e que seguidamente mostre
no ecrã as ocorrências de cada vogal. Por exemplo, digitando a frase Campus
Lumiar, a resposta deve ser:
Ocorrências da Vogal a: 2
Ocorrências da Vogal e: 0
Ocorrências da Vogal i: 1
Ocorrências da Vogal o: 0
Ocorrências da Vogal u: 2
'''

vogais = ['a','e','i','o','u']
vogais_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'â','ê', 'ô', 'à' , 'ã']

plvr = str(input('Digite uma palavra: '))
print(plvr)


for vogal in vogais:
    contador = plvr.count(vogal)
    print(f'Ocorrências da Vogal {vogal}: {contador}')
# Para verificar se há ou não acentos
for vogal in vogais_acentuadas:
    ocorrencias = plvr.count(vogal)
    if ocorrencias > 0:
        print(f'Ocorrências da Vogal {vogal}: {ocorrencias}')

