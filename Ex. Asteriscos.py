def asteriscos():
    num_linhas = int(input("Escreve um número: "))
        # Verificar se o número é positivo
    if num_linhas <= 0:
        print("Apenas inteiros positivos.")
        return
    # Usar um ciclo para desenhar o padrão de asteriscos
    for i in range(1, num_linhas + 1):
        print('*' * i)

asteriscos()
