'''
Crie um programa que leia três valores inteiros digitados para três variáveis,
nomeadamente, n1, n2 e n3 e que, seguidamente, determine qual é o seu valor
intermédio.
Nota:
Não é a média que é pedida, mas sim o valor do intermédio!
Assim, por exemplo, dados os valores: 7, 8 e 6, digitados para as variáveis n1, n2 e n3,
respetivamente, a resposta é 7 (o valor 7 está no meio de 6 e 8). Por sua vez, no caso de
serem digitados os valores 9, 3 e 5, para as variáveis n1, n2 e n3, respetivamente, a
resposta é 5. Use uma estrutura condicional (ou seja, não pode ordenar os números e
ler o valor que está no meio dos três).
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 <= n2 <= n3 or n3 <= n2 <= n1:
    valor_intermedio = n2
elif n2 <= n1 <= n3 or n3 <= n1 <= n2:
    valor_intermedio = n1
else:
    valor_intermedio = n3

print(f"A mediana é: {valor_intermedio}")