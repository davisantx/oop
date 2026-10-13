# ----------------------------------------------------------------------------------------
# Tecnologia em Análise e Desenvolvimento de Sistemas, IFCE Campus Itapipoca (2026.2)
# Docente: Eduardo Olivindo
# Discente: Davi Santos (@davisantx)
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Detalhes:
#   Para executar a implementação de cada questão, chame as funções: q1, q2, q3, q4...
#
#   Ex.: Quero visualizar apenas as questões 2 e 3:
#       q2()
#       q3()
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------

def intro(num_questao: int) -> None:
    print(f"QUESTÃO {num_questao}: \n")

def fim() -> None:
    print("\n\n")

# Questões:

# Q1
class Lampada:
    def __init__(self):
        self.__ligado = False
        print("A lâmpada está desligada!")

    def ligar(self):
        self.__ligado = True
        print("A lâmpada está ligada!")

    def desligar(self):
        self.__ligado = False
        print("A lampada está desligada!")


def q1():
    intro(1)
    l1 = Lampada()
    l1.ligar()
    l1.ligar()
    l1.desligar()
    l1.ligar()
    fim()

# Q2
class Ponto:
    def __init__(self, nome: str, x: int, y: int):
        self.__nome = nome
        self.__x = x
        self.__y = y

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        pass
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor: int):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor: int):
        pass

    def __str__(self) -> str:
        return f"{self.__nome}: ({self.__x}, {self.__y})"

    def calcular_distancia(self, ponto: "Ponto") -> float:
        return (((self.__x - ponto.__x) ** 2) + (self.__y - ponto.__y)) ** 0.5


def entrada(numero: int) -> tuple[int, int]:
    x: int = 0
    y: int = 0

    while True:
        try:
            x = int(input(f"x{numero}: "))
            y = int(input(f"y{numero}: "))
        except ValueError:
            continue
        return x, y

def q2(quantidade_de_pontos: int):
    intro(2)

    pontos = []

    for i in range(quantidade_de_pontos):
        x, y = entrada(i + 1)

        if x is None or y is None:
            continue

        ponto = Ponto(f"Ponto {i + 1}", x, y)
        pontos.append(ponto)

    print()
    for ponto in pontos:
        print(ponto)
    fim()


# Q3
def q3(quantidade_de_pares_de_pontos: int):
    print("QUESTÃO 3\n\n")

    pontos: list[tuple[Ponto, Ponto]] = []

    for i in range(quantidade_de_pares_de_pontos):
        print(f"Distância do Ponto {i + 1} em relação ao Ponto {i + 2}\n")

        print(f"Insira as posições do Ponto {i + 1}: \n")
        x_a, y_a = entrada(i + 1)

        print(f"\nInsira as posições do Ponto {i + 2}: \n")
        x_b, y_b = entrada(i + 2)

        ponto_a = Ponto(f"Ponto {i + 1}", x_a, y_a)
        ponto_b = Ponto(f"Ponto {i + 2}", x_b, y_b)

        pontos.append((ponto_a, ponto_b))

    print()
    for par_pontos in pontos:
        print(
            f"Distância entre {par_pontos[0].nome} e {par_pontos[1].nome}: {par_pontos[0].calcular_distancia(par_pontos[1]):.2f}"
        )

    fim()


# Q4
class Funcionario:
    def __init__(self, nome: str, cargo: str, valor_da_hora_trabalhada: float = 100):
        if not isinstance(nome, str):
            raise TypeError("Erro! Nome deve ser texto!")
        if not isinstance(cargo, str):
            raise TypeError("Erro! Cargo deve ser texto!")
        if not isinstance(valor_da_hora_trabalhada, (float | int)):
            raise TypeError("Erro! Valor da hora trabalhada deve ser número!")
        
        self.nome = nome
        self.cargo = cargo
        self.valor_da_hora_trabalhada = valor_da_hora_trabalhada
        self.__quantidade_de_horas_trabalhadas = 0
        self.__salario = 0

    def registrar_uma_hora_de_trabalho(self) -> None:
        self.__quantidade_de_horas_trabalhadas += 1

    def __calcular_o_salario(self) -> float:
        return self.__quantidade_de_horas_trabalhadas * self.valor_da_hora_trabalhada
        
    @property
    def salario(self) -> float:
        self.__salario = self.__calcular_o_salario()
        return self.__salario

    @salario.setter
    def salario(self, valor: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Nome: {self.nome} | Cargo: {self.cargo} | Salário: {self.salario}"


def q4():
    intro(4)

    f1 = Funcionario(
        nome="João", 
        cargo="Cozinheiro", 
        valor_da_hora_trabalhada=85
    )
    f2 = Funcionario(
        nome="Maria", 
        cargo="Gerente bancária", 
        valor_da_hora_trabalhada=120
    )

    # f1.salario = 5032 # Inválido

    for i in range(40 * 4):
        f1.registrar_uma_hora_de_trabalho()

    print(f1.salario)

    for i in range(40 * 5):
        f2.registrar_uma_hora_de_trabalho()

    print(f2.salario)

    fim()


# Q5
class Elevador:
    def __init__(self, capacidade: int, total_andares: int):
        self.__andar_atual = 0

        if not isinstance(capacidade, int):
            raise TypeError("Erro! A capacidade do elevador deve ser um número inteiro!")
        if not isinstance(total_andares, int):
            raise TypeError("Erro! Número total de andares deve ser um número inteiro!")
            
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__quantidade_pessoas = 0

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, valor: int) -> None:
        self.__verificar_se_nao_e_inteiro(valor, "O andar atual")
        self.__verificar_se_e_negativo(valor, "O andar atual")

        self.__andar_atual = valor

    @property
    def total_andares(self) -> int:
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, valor: int) -> None:
        self.__verificar_se_nao_e_inteiro(valor, "O total de andares")
        self.__verificar_se_e_negativo(valor, "O total de andares")

        self.__total_andares = valor

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, valor: int) -> None:
        self.__verificar_se_nao_e_inteiro(valor, "A capacidade")
        self.__verificar_se_e_negativo(valor, "A capacidade")

        self.__capacidade = valor

    @property
    def quantidade_pessoas(self) -> int:
        return self.__quantidade_pessoas

    @quantidade_pessoas.setter
    def quantidade_pessoas(self, valor: int) -> None:
        self.__verificar_se_nao_e_inteiro(valor, "A quantidade de pessoas")
        self.__verificar_se_e_negativo(valor, "A quantidade de pessoas")

        self.__quantidade_pessoas = valor

    def __verificar_se_nao_e_inteiro(self, valor, nome: str):
        if not isinstance(valor, int):
            raise TypeError(f"Erro! {nome} deve ser um número inteiro!")

    def __verificar_se_e_negativo(self, valor, nome: str):
        if valor < 0:
            raise ValueError(f"Erro! {nome} não pode ser um número negativo!")

    def entrar(self) -> None:
        if self.quantidade_pessoas >= self.capacidade:
            raise ValueError("Erro! O elevador está cheio!")

        self.quantidade_pessoas += 1

    def subir(self) -> None:
        if self.andar_atual >= self.total_andares:
            raise ValueError("Erro! O elevador está no último andar!")

        self.andar_atual += 1

    def descer(self) -> None:
        if self.andar_atual <= 0:
            raise ValueError("Erro! O elevador já está no terreo!")

        self.andar_atual -= 1

    def sair(self):
        if self.quantidade_pessoas <= 0:
            raise ValueError("Erro! O elevador já está vázio!")

        self.quantidade_pessoas -= 1

    def __str__(self) -> str:
        return f"Andar atual: {self.andar_atual} | Capacidade: {self.capacidade} | Total de andares: {self.total_andares} | Quantidade de pessoas: {self.quantidade_pessoas}"


def q5():
    # Testar todas as características da classe 'Elevador'
    intro(5)
    print("Elevador 1: \n")
    e1 = Elevador(5, 3)
    print(e1)
    e1.entrar()
    print(e1)
    e1.subir()
    print(e1)
    e1.descer()
    print(e1)
    e1.sair()
    print(e1)

    print("\nElevador 2: \n")
    e2 = Elevador(7, 6)

    for i in range(7):
        e2.entrar()

    e2.subir()
    e2.subir()

    try:
        e2.entrar()
    except ValueError as e:
        print(e)
    print(e2)
    fim()


# Q6
class Recording:
    def __init__(self, duracao: int=0):
        if not isinstance(duracao, int):
            raise TypeError("Erro! Duração deve ser um número inteiro!")
        if duracao < 0:
            raise ValueError("Erro! Duração não pode negativo!")
        self.__length = duracao

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError("Erro! Duração deve ser um número inteiro!")
        if valor < 0:
            raise ValueError("Erro! Duração não pode negativo!")

        self.__length = valor
        

def q6():
    intro(6)
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
    fim()


# Q7
class WeatherStation:
    def __init__(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Erro! Nome deve ser texto!")
            
        self.__nome = nome
        self.__observations: list[str] = []

    def add_observation(self, observation: str) -> None:
        if not isinstance(observation ,str):
            raise TypeError("Error!")
        self.__observations.append(observation)

    def lastest_observation(self) -> str:
        if not self.__observations:
            return ""
        return self.__observations[self.number_of_observations() - 1]

    def number_of_observations(self) -> int:
        return len(self.__observations)

    def __str__(self) -> str:
        return f"{self.__nome}, {self.number_of_observations()} observations"


def q7():
    intro(7)
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")

    print(station.lastest_observation())

    station.add_observation("Thunderstorm")
    print(station.lastest_observation())

    print(station.number_of_observations())
    print(station)


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Chamada de cada questão:
if __name__ == "__main__":
    q1()
    q2(quantidade_de_pontos=3)
    q3(quantidade_de_pares_de_pontos=1)
    q4()
    q5()
    q6()
    q7()
# ----------------------------------------------------------------------------------------
