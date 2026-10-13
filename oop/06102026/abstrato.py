from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Retangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


r1 = Retangulo(3, 3)

print(r1.area())