'''
Faça um programa para converter uma temperatura de grau Celsius para Fahrenheit,
usando uma função, criada por si (ou seja, o programa principal deve passar à função o
valor de graus centígrados a converter e esta deve devolvê-lo o valor correspondente
em Fahrenheit). Finalmente e, por sua vez, o programa chamante deve imprimir o valor
convertido recebido.
Fórmula: °F = °C x 1.8 + 32.
'''
def celsiusToFahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsiusToFahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
    except ValueError:
        print("Valor inválido! Por favor, digite um número.")
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsiusToFahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
        
if __name__ == "__main__":
    main()
