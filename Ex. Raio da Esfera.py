import math

def calcular_Volume():
    raio = float(input("Qual é o raio da esfera? \n"))
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

volume_esfera = calcular_Volume()
print(f'O volume da esfera é: {volume_esfera}')