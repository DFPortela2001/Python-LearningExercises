'''
Escreva um programa para calcular o ordenado líquido de um empregado de uma
determinada firma que é pago consoante o número de horas que trabalhou.
As Taxas são as seguintes.
IRS = 20% se salário bruto >= 1000€.
15% se salário bruto >= 600€ e < 1000€.
10% se salário bruto < 600€.
Horas Extras = acima de 35H cada Hora vale 1,5H (incluindo horas trabalhadas durante
o fim de semana).
Segurança Social = 11% sobre o salário bruto.

O programa deve pedir para digitar o seguinte:
Número do empregado.
Número de horas que o empregado trabalhou.
Valor Hora que o empregado é pago.
'''
numero_empregado = int(input("Número do empregado: "))
horas_trabalhadas = float(input("Número de horas trabalhadas: "))
valor_hora = float(input("Valor Hora: "))

salario_bruto = horas_trabalhadas * valor_hora

if horas_trabalhadas > 35:
    salario_bruto += (horas_trabalhadas - 35) * valor_hora * 1.5

irs = 0
if salario_bruto >= 1000:
    irs = 0.2
elif salario_bruto >= 600:
    irs = 0.15
else:
    irs = 0.1

seguranca_social = 0.11 * salario_bruto

salario_liquido = salario_bruto - (irs * salario_bruto) - seguranca_social

print(f"Ordenado líquido do empregado: {salario_liquido:.2f}€")
print(f"Ordenado bruto do empregado: {salario_bruto:.2f}€")
print(f"O salário previsto ao fim do mes é de :  {(salario_liquido*4)}")
