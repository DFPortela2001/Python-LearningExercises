class Empregado:
    def __init__(self, numero, nome, sal_Bruto):
        self.__numero = numero       # atributo privado
        self._nome = nome            # atributo protegido
        self.sal_Bruto = sal_Bruto
        self.sal_Liquido = 0.0
        self.taxa_IRS = 0.0
        self.taxa_SS = 0.11

    def calcIRS(self):
        if self.sal_Bruto >= 2000.00:
            self.taxa_IRS = 0.25
        elif self.sal_Bruto >= 1000.00:
            self.taxa_IRS = 0.20
        else:
            self.taxa_IRS = 0.175

    def calcSS(self):
        pass

    def calc_Sal_Liquido(self):
        self.calcIRS()
        self.calcSS()
        valorIRS = self.sal_Bruto * self.taxa_IRS
        valorSS = self.sal_Bruto * self.taxa_SS
        self.sal_Liquido = self.sal_Bruto - (valorIRS + valorSS)
        return valorIRS, valorSS

    def __str__(self):
        valorIRS, valorSS = self.calc_Sal_Liquido()
        return (f"Empregado:\n"
                f"Numero: {self.__numero}\n"
                f"Nome: {self._nome}\n"
                f"Salário Bruto: {self.sal_Bruto:.2f}\n"
                f"Desconto IRS: {valorIRS:.2f}\n"
                f"Desconto Segurança Social: {valorSS:.2f}\n"
                f"Salário Líquido: {self.sal_Liquido:.2f}\n")

class Professor(Empregado):
    def __init__(self, numero, nome, sal_Bruto, area_Ensino):
        super().__init__(numero, nome, sal_Bruto)
        self.area_Ensino = area_Ensino

    def __str__(self):
        valorIRS, valorSS = self.calc_Sal_Liquido()
        return (f"Professor:\n"
                f"Numero: {self._Empregado__numero}\n"  # Acesso ao atributo privado da classe base
                f"Nome: {self._nome}\n"
                f"Área de Ensino: {self.area_Ensino}\n"
                f"Salário Bruto: {self.sal_Bruto:.2f}\n"
                f"Desconto IRS: {valorIRS:.2f}\n"
                f"Desconto Segurança Social: {valorSS:.2f}\n"
                f"Salário Líquido: {self.sal_Liquido:.2f}\n")

def main():
    # Criando objeto emp1
    emp1 = Empregado(12345, "Ana Rita", 2500.00)
    emp1.calc_Sal_Liquido()
    print(f"Dados Objeto emp1:\n{emp1}")

    # Criando objeto prof1
    prof1 = Professor(33366, "Rui Alves", 1800.00, "Matemática")
    prof1.calc_Sal_Liquido()
    print(f"Dados Objeto prof1:\n{prof1}")

if __name__ == "__main__":
    main()
