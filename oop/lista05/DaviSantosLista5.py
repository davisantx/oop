# ----------------------------------------------------------------------------------------
# Tecnologia em Análise e Desenvolvimento de Sistemas, IFCE Campus Itapipoca (2026.2)
# Docente: Eduardo Olivindo
# Discente: Davi Santos (@davisantx)
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Para executar a implementação de cada questão, chame as funções: q1, q2, q3, q4...
# 
# Ex.:
#   q2()
#   q3()
# ----------------------------------------------------------------------------------------
def intro(num_questao: int) -> None:
    print(f"QUESTÃO {num_questao}: \n")

def fim() -> None:
    print("\n\n")
# ----------------------------------------------------------------------------------------
# Questões:
# Q1





class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar_detalhes(self):
        return f"Nome: {self.nome} - idade: {self.idade}"


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar_detalhes(self):
        return f"{super().apresentar_detalhes()} - Matrícula: {self.matricula}"


def q1():
    intro(1)
    aluno = Aluno("Ana", 20, "2026001")
    print(aluno.apresentar_detalhes())
    fim()


# Q2

class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

    def calcular_pagamento(self) -> float:
        return 1621


class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, horas, valor_hora: float):
        super().__init__(nome)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_pagamento(self) -> float:
        return self.horas * self.valor_hora

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, salario_fixo: float, comissao: float):
        super().__init__(nome)
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_pagamento(self) -> float:
        return self.salario_fixo + self.comissao

def exibir_salarios(funcionarios: list[Funcionario]):
    for funcionario in funcionarios:
        print(f"Nome: {funcionario.nome} Salário: {funcionario.calcular_pagamento():.2f}")

def q2():
    intro(2)

    funcionarios = [
        FuncionarioHorista(nome="João", horas=44 * 4, valor_hora=20),
        FuncionarioComissionado(nome="Isabela", salario_fixo=1500, comissao=21)
    ]

    exibir_salarios(funcionarios)
    fim()

# Q3

class Disciplina:
    def __init__(self, nome: str, carga_horaria: int):
        self.nome = nome
        self.carga_horaria = carga_horaria

class PessoaQ3:
    def __init__(self, nome: str, cpf):
        self.nome = nome
        self.cpf = cpf


class Servidor(Pessoa):
    def __init__(self, nome: str, cpf, codigo_siape):
        super().__init__(nome, cpf)
        self.codigo_siape = codigo_siape


class Professor(Servidor):
    def __init__(self, nome: str, cpf, codigo_siape, disciplinas: list[Disciplina]):
        super().__init__(nome, cpf, codigo_siape)
        self.disciplinas = disciplinas

class TAE(Servidor):
    def __init__(self, nome: str, cpf, codigo_siape, funcao: str):
        super().__init__(nome, cpf, codigo_siape)
        self.funcao = funcao

class AlunoQ3(Pessoa):
    def __init__(self, nome: str, cpf, matricula, curso, disciplinas: list[Disciplina]):
        super().__init__(nome, cpf)
        self.matricula= matricula
        self.curso = curso
        self.disciplinas = disciplinas


# Q4
# 
class Computer: pass

class Laptop(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        """
        speed: MHz
        weight: Kg
        """
        self.model = model
        self.speed = speed
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f"{self.model}, {self.speed} MHz, {self.__weight} Kg"

def q4():
    intro(4)
    laptop = Laptop("Notebook Pro", 1500, 2)
    print(laptop)
    fim()


# Q5

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self) -> str:
        return f"Width: {self.width} | Height: {self.height}"

class Square(Rectangle):
    def __init__(self, width: float, height: float):
        super().__init__(width, height)

    def area(self):
        return super().area()


# Q6
class Pagamento:
    def processar(self):
        print("Processando pagamento...")

class PagamentoPix(Pagamento):
    def processar(self):
        print("Processando pagamento pix...")

class PagamentoCartao(Pagamento):
    def processar(self):
        print("Processando pagamento cartão...")

class Compra:
    def __init__(self, nome_produto: str, tipo_de_pagamento: Pagamento):
        self.nome_produto = nome_produto
        self.tipo_de_pagamento = tipo_de_pagamento

    
def comprar(compras: list[Compra]):
    for i, compra in enumerate(compras):
        print(f"Produto {i + 1}: {compra.nome_produto}")
        compra.tipo_de_pagamento.processar()

def q6():
    intro(6)
    comprar([
        Compra(nome_produto="Iphone 15", tipo_de_pagamento=PagamentoPix()),
        Compra(nome_produto="Casaco x248", tipo_de_pagamento=PagamentoCartao()),
    ])
    fim()


# Q7

class CartaoMensagem:
    def __init__(self, destinario, remetente):
        self.destinatario = destinario
        self.remetente = remetente

    def retornar_mensagem(self):
        pass

class CartaoDiaDosNamorados(CartaoMensagem): 
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return super().retornar_mensagem()


class CartaoNatal(CartaoMensagem): 
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return super().retornar_mensagem()


class CartaoAniversario(CartaoMensagem): 
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return super().retornar_mensagem()

# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Chamada de cada questão:
if __name__ == "__main__":
    q1()
    # q2()
    # q3()
    q4()
    # q5()
    q6()
# ----------------------------------------------------------------------------------------