from abc import ABC, abstractmethod

class Empregado(ABC):
    def __init__(self, nome, id, salBruto):
        self.nome = nome
        self.id = id
        self.salBruto = salBruto
        self.salLiquido = 0.0

    @abstractmethod
    def calcSS(self, taxaSS):
        pass

    def calcIRS(self, taxaIRS):
        return self.salBruto * taxaIRS

class Medico(Empregado):
    def __init__(self, nome, id, salBruto, especialidade):
        super().__init__(nome, id, salBruto)
        self.especialidade = especialidade

    def calcSS(self, taxaSS):
        return self.salBruto * taxaSS

# Criação do objeto medico1 e cálculo do salário líquido
medico1 = Medico(nome="Ivo Reis", id=45000, salBruto=2400.75, especialidade="Ortopedista")
medico1.salLiquido = medico1.salBruto - (medico1.calcIRS(0.25) + medico1.calcSS(0.11))

# Impressão dos dados do objeto medico1
print("\nDados do objeto medico1:")
print(f"Nome: {medico1.nome}")
print(f"ID: {medico1.id}")
print(f"Especialidade: {medico1.especialidade}")
print(f"Salário Bruto: {medico1.salBruto}")
print(f"Salário Líquido: {medico1.salLiquido:.2f}")
