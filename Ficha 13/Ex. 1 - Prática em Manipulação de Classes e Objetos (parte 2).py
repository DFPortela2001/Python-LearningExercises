'''
Na continuação do programa anterior (Ficha 012), crie uma subclasse Professor
com o seu próprio atributo:

areaEnsino

E obtenha agora todos os cálculos (Salários Bruto e Líquido, bem como os valores
IRS e SS) para um objeto instanciado a partir desta classe derivada, repetindo
assim o programa anterior incluindo a classe herdada.
'''

class Empregado:
    def __init__(self, numero, nome, sal_Bruto):
        self.numero = numero
        self.nome = nome
        self.sal_Bruto = sal_Bruto
        self.sal_Liquido = 0.0
        self.taxa_IRS = 0.0
        self.taxa_SS = 0.11

#CALCULAR A TAXA DE IRS A SER USADA
    def calcIRS(self):
        if self.sal_Bruto >= 2000.00:
            self.taxa_IRS = 0.25
        elif self.sal_Bruto >= 1000.00:
            self.taxa_IRS = 0.20
        else:
            self.taxa_IRS = 0.175
#SEGURANÇA SOCIAL TEM TAXA FIXA 11%    
    def calcSS(self):
        pass
#CALCULAR SALARIO LIQUIDO   
    def calc_Sal_Liquido(self):
        self.calcIRS()
        self.calcSS()
        valorIRS = self.sal_Bruto * self.taxa_IRS
        valorSS = self.sal_Bruto * self.taxa_SS
        self.salLiquido = self.sal_Bruto - (valorIRS + valorSS)
        return valorIRS, valorSS
#FORMA DE IMPRIMIR A CLASSE    
    def __str__(self):
        return (f"Empregado: \n{self.nome} - Nº {self.numero}\n"
                f"Salário Bruto: {self.sal_Bruto:.2f}\n"
                f"Taxa IRS: {self.taxa_IRS * 100:.2f}%\n"
                f"O valor de IRS pago é: {self.taxa_IRS * self.sal_Bruto}\n"
                f"Taxa Segurança Social: {self.taxa_SS * 100:.2f}%\n"
                f"O valor de Segurança Social pago é: {self.taxa_SS * self.sal_Bruto}\n"
                f"Salário Líquido: {self.salLiquido:.2f}")

class Professor(Empregado):
    def __init__(self, numero, nome, sal_Bruto, area_Ensino):
        super().__init__(numero, nome, sal_Bruto)
        self.area_Ensino = area_Ensino
    
    def __str__(self):
        return (f"Professor: \n{self.nome} - Nº {self.numero}\n"
                f"Área de Ensino: {self.area_Ensino}\n"
                f"Salário Bruto: {self.sal_Bruto:.2f}\n"
                f"Taxa IRS: {self.taxa_IRS * 100:.2f}%\n"
                f"O valor de IRS pago é: {self.taxa_IRS * self.sal_Bruto}\n"
                f"Taxa SS: {self.taxa_SS * 100:.2f}%\n"
                f"O valor de Segurança Social pago é: {self.taxa_SS * self.sal_Bruto}\n"
                f"Salário Líquido: {self.salLiquido:.2f}")


def main():
    aux = input('Está a adicionar um empregado ou professor? (Escreva "empregado" ou "professor") \n')
    if aux.lower() == 'empregado':
        numero = int(input('Insira o número do empregado: '))
        nome = input('Insira o nome do empregado: ')
        sal_Bruto = float(input('Quanto é o salário bruto do empregado? '))
        empregado = Empregado(numero, nome, sal_Bruto)
        empregado.calc_Sal_Liquido()
        print(empregado)
    elif aux.lower() == 'professor':                        
        numero = int(input('Escreva o número do professor: '))
        nome = input('Escreva o nome do professor: ')
        sal_Bruto = float(input('Quanto é o salário bruto do professor? '))
        area_Ensino = input("Escreva a área de ensino do professor: ")
        professor = Professor(numero, nome, sal_Bruto, area_Ensino)
        professor.calc_Sal_Liquido()
        print(professor)

if __name__ == "__main__":
    main()
