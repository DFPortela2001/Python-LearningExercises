def contador_valores(lista):
    contador = 0
    for valor in lista:
        if valor > 20.00:
            contador += 1
    return contador

def main():
    vetor = []
    for i in range(5):
        valor = float(input(f"Escreva os valores {i + 1} (float): "))
        vetor.append(valor)

    acima_20 = contador_valores(vetor)
    
    print(f"O número de valores acima de 20.00 é: {acima_20}")


if __name__ == "__main__":
    main()
