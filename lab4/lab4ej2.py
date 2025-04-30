import random
import math
from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color):
        self.color = color
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    def __str__(self):
        return f"Color: {self.color}"
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Rojo"):
        super().__init__(color)
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado
    def comoColorear(self):
        return "Colorear los cuatro lados"
    def __str__(self):
        return f"Cuadrado - {super().__str__()}, Lado: {self.lado}"

class Circulo(Figura):
    def __init__(self, radio, color="Azul"):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Circulo - {super().__str__()}, Radio: {self.radio}"


def main():
    figuras = []
    for i in range(5):
        tipo = random.randint(1, 2) 
        valor = round(random.uniform(1, 10), 2)
        if tipo == 1:
            figura = Cuadrado(valor)
        else:
            figura = Circulo(valor)

        figuras.append(figura)
    for fig in figuras:
        print(fig)
        print(f"Área: {fig.area():.2f}")
        print(f"Perímetro: {fig.perimetro():.2f}")
        if isinstance(fig, Coloreado):
            print(f"Como colorear: {fig.comoColorear()}")
        print("-" * 40)

main()
