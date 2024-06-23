'''
Escreva um programa que crie uma matriz 3X4 (3 linhas/4 colunas) de valores
inteiros e passe-a a uma função para que devolva a quantidade de valores
negativos nela contidos. Por sua vez, o programa chamante deve imprimir no
ecrã o valor devolvido.
'''

def valores_negativos(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor < 0:
                contador += 1
    return contador

def main():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(4):
            valor = int(input(f"Escreva o valor para a posição [{i+1},{j+1}] da matriz: "))
            linha.append(valor)
        matriz.append(linha)
    
    result = valores_negativos(matriz)
    print(f"Número de valores negativos na matriz: {result}")
    for aux in range(3):
        print(matriz[aux])

if __name__ == "__main__":
    main()
