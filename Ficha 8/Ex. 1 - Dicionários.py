'''
Crie um dicionário para guardar informação sobre animais de estimação.
Cada chave é o nome de um animal e cada valor é a espécie de animal.
Por exemplo: 'Ziggy': 'canário'.

1. Comece por definir um dicionário base com os seguintes cinco pares chave-
valor:

Ziggy: canario, Pluto: cao, Kitty: gato, Nemo: peixe, Mickey: rato
2. Seguidamente, peça ao utilizador para adicionar dados de novos animais.
Deverá parar a inserção quando o utilizador inserir a palavra 'fim'.

3. Desenvolva um mecanismo de pesquisa que imprima um determinado par
Chave-Valor a pedido do utilizador, a partir de uma dada chave.
'''


dic={'Ziggy': 'canário', 'Pluto': 'cao', 'Kitty': 'gato', 'Nemo': 'peixe', 'Mickey': 'rato'}
print("Dicionário base:")
print(dic)
while True:
    nome=input('Insira o nome do novo animal (ou "fim" para parar de inserir): \n')
    if nome.lower() == 'fim':
        break
    else:
        especie=input('Qual é a espécie do animal: ')
        dic[nome]=especie
        print('Dicionário atualizado: \n')
        print(dic)
while True:
    print("Pesquisa de animais: ")
    pesquisa=input('Insira o nome do animal para pesquisar (ou "fim" para parar de pesquisar): \n')
    if pesquisa.lower() == 'fim':
        break
    if pesquisa in dic.keys():
        print(f"O {pesquisa} é um {dic[pesquisa]}")
    else:
        print(f'O {pesquisa} não foi encontrado')


