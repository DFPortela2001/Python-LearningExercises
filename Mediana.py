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