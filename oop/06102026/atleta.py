class T:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def dizer_oi(self):
        print(f"Oi! Sou o {self.nome}")

class Atleta(T):
    def __init__(self, nome: str, idade: int, peso: int):
        super().__init__(nome, idade)
        self.peso = peso

    def aquecer(self):
        print("Aquecendo")

class Corredor(Atleta):
    def correr(self):
        print("Correndo...")

class Nadador(Atleta):
    def nadar(self):
        print("Nadando...")

class Ciclista(Atleta):
    def pedalar(self):
        print("Pedalando...")

class Triatleta(Corredor, Nadador, Ciclista):
    pass

t = Triatleta("Davi", 24, 23)

t.pedalar()
t.aquecer()
t.dizer_oi()