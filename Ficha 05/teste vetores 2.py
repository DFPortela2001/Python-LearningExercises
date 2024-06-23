def calcular_soma_e_contar_valores_acima_de_20(vetor):
    contador = 0
    soma = 0.0
    valores_acima_de_20 = []
    for valor in vetor:
        if valor > 20.00:
            contador += 1
            soma += valor
            valores_acima_de_20.append(valor)
    return contador, soma, valores_acima_de_20

def main():
    vetor = []
    for i in range(5):
        valor = float(input(f"Digite o valor {i+1} de 5: "))
        vetor.append(valor)
    
    contador, soma, valores_acima_de_20 = calcular_soma_e_contar_valores_acima_de_20(vetor)
    print(f"Número de valores acima de 20.00: {contador}")
    print(f"Soma dos valores acima de 20.00: {soma}")
    print(f"Valores acima de 20.00: {valores_acima_de_20}")

if __name__ == "__main__":
    main()
