'''
Escreva um programa que leia sete valores de temperaturas digitados (use um ciclo) e
que seguidamente calcule as médias das temperaturas cujos valores estejam
compreendidos entre 18 e 28 graus, ambos inclusive, bem como de todas as
temperaturas. Portanto, é pedido os cálculos de duas médias, uma dos valores entre 18
e 28 graus e outra de todos os valores (incluindo assim os que estejam também entre
18 e 28 graus).
'''

temperaturas = []
for i in range(7):
    try: 
        temperatura = float(input(f"Escreva a {i+1}ª temperatura: "))
    except:
        print('Só podes meter números')
    finally:
        temperatura = 0
    temperaturas.append(temperatura)
    

soma_total = 0
contador_total = 0
soma_entre_18_e_28 = 0
contador_entre_18_e_28 = 0

for temperatura in temperaturas:
    soma_total += temperatura
    contador_total += 1
    if temperatura >= 18 and temperatura <= 28:
        soma_entre_18_e_28 += temperatura
        contador_entre_18_e_28 += 1

media_total = soma_total / contador_total if soma_total != 0 else 0
media_entre_18_e_28 = soma_entre_18_e_28 / contador_entre_18_e_28 if soma_entre_18_e_28 != 0 else 0 

if media_total == soma_total == 0:
    print(f"A temperatura média é: {soma_total}")
else:
    print(f"Média de todas as temperaturas: {media_total:.2f}")
if media_entre_18_e_28 == soma_entre_18_e_28 == 0:
    print("Por favor introduza valores válidos para a soma entre 18º e 28º")
else:
    print(f"Média das temperaturas entre 18 e 28 graus: {media_entre_18_e_28:.2f}")
