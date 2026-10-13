from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def perimetro(self) -> float:
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    def perimetro(self):
        return 2 * (self.base * self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def perimetro(self):
        return 2 * 3.14 * self.raio

class Triangulo(FiguraGeometrica):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c

r1 = Retangulo(200, 100)
c1 = Circulo(100)
t1 = Triangulo(2, 3, 4)

print(r1.perimetro())
print(c1.perimetro())
print(t1.perimetro())