'''
Crie um programa que leia três valores inteiros digitados para três variáveis,
nomeadamente, n1, n2 e n3 e que, seguidamente, passe-os a uma função criada por si,
a fim de determinar qual o seu valor intermédio e devolvê-lo ao programa chamante
que, por sua vez, deve mostrar o resultado devolvido no ecrã.
'''

def mediana(n1, n2, n3):
    if n1 <= n2 <= n3 or n3 <= n2 <= n1:
        return n2
    elif n2 <= n1 <= n3 or n3 <= n1 <= n2:
        return n1
    else:
        return n3

def main():
    n1 = int(input("Digite o primeiro valor inteiro: "))
    n2 = int(input("Digite o segundo valor inteiro: "))
    n3 = int(input("Digite o terceiro valor inteiro: "))

    valor_intermedio = mediana(n1, n2, n3)
    print(f"O valor intermédio é: {valor_intermedio}")

if __name__ == "__main__":
    main()
