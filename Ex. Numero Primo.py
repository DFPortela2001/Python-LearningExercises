'''
Crie um programa, que use uma função, criada por si, para testar se um determinado
número passado como parâmetro é ou não primo. A função deve devolver o valor 1 ao
programa chamante no caso de o número ser primo ou o valor 0 no caso de não o ser.
Por sua vez, o programa chamante deve informar no ecrã se o número em análise é
ou não primo.
'''

def verificar_primo(numero):
    if numero <= 1:
        return 0  # Não é primo se for menor ou igual a 1
    elif numero == 2:
        return 1  # 2 é primo
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return 0  # Não é primo se for divisível por algum número além de 1 e ele mesmo
        return 1  # É primo se não for divisível por nenhum

def main():
    numero = int(input("Digite um número para verificar se é primo: "))
    
    if verificar_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

if __name__ == "__main__":
    main()