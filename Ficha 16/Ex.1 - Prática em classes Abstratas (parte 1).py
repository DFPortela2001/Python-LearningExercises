from abc import ABC, abstractmethod
import math

class MinhaAbstrata(ABC):
    def __init__(self, raio):
        self.raio = raio

    @abstractmethod
    def calcArea(self):
        pass

    def calcDiam(self):
        return 2 * self.raio

    def calcVolume(self):
        return (4/3) * math.pi * self.raio**3

class Esfera(MinhaAbstrata):
    def __init__(self, raio):
        super().__init__(raio)

    def calcArea(self):
        return 4 * math.pi * self.raio**2

    def __str__(self):
        return (f"Esfera com raio {self.raio}:\n"
                f"Área: {self.calcArea():.2f}\n"
                f"Diâmetro: {self.calcDiam():.2f}\n"
                f"Volume: {self.calcVolume():.2f}\n")


def main():
    raio = float(input("Digite o raio da esfera: "))
    esfera = Esfera(raio)
    print(esfera)

if __name__ == "__main__":
    main()
