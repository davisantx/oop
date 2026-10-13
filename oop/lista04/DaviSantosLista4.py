import os
from random import randint, random, shuffle
from time import sleep

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
def intro(num_questao: int) -> None:
    print(f"QUESTÃO {num_questao}: \n")

def fim() -> None:
    print("\n\n")
# ----------------------------------------------------------------------------------------

# Questões:
# Q1
class Pet:
    def __init__(self, name: str, c: str):
        self.__name = name
        self.__c = c

    def __str__(self) -> str:
        return f"{self.__name}, a {self.__c}"

class Person:
    def __init__(self, name: str, pet: Pet):
        if not isinstance(name, str):
            raise TypeError("Error")

        if not isinstance(pet, Pet):
            raise TypeError("Error")
            
        self.__name = name
        self.__pet = pet

    def __str__(self) -> str:
        return f"{self.__name}, his pet is {self.__pet}"


def q1() -> None:
    intro(1)
    hulda = Pet("Hulda", "mixed breed")
    hesi = Person("Hexi", hulda)
    print(hesi)
    fim()

# Q2
class Present:
    def __init__(self, name: str, weight: int):
        if not isinstance(name, str):
            raise TypeError()

        self.__name = name

        if not isinstance(weight, int):
            raise TypeError()
        
        self.__weight = weight

    @property
    def weight(self) -> int:
        return self.__weight

class Box:
    def __init__(self):
        self.__presents: list[Present] = []

    def add_present(self, present: Present) -> None:
        self.__presents.append(present)

    def total_weight(self) -> int:
        weight = 0
        for present in self.__presents:
            weight += present.weight
        return weight

def q2() -> None:
    intro(2)
    book = Present("ABC Book", 2)
    box = Box()
    box.add_present(book)
    print(box.total_weight())
    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
    fim()

# Q3
class Contato:
    def __init__(self, nome: str, telefone: int):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self) -> str:
        return self.__nome

    def __str__(self) -> str:
        return f"Nome: {self.__nome} | Telefone: {self.__telefone}"

    def __repr__(self) -> str:
        return f"Nome: {self.__nome} | Telefone: {self.__telefone}"
        
class Agenda:
    def __init__(self):
        self.__contatos: list[Contato] = []
        
    def adicionar_contato(self, contato: Contato) -> None:
        if not isinstance(contato, Contato):
            raise TypeError("Erro! Contato deve ser um contato!")
        self.__contatos.append(contato)
        
    def remover_contato(self, nome_do_contato: str) -> None:
        for contato in self.__contatos:
            if nome_do_contato == contato.nome:
                self.__contatos.remove(contato)
                return

    def __str__None(self) -> str:
        return f"{self.__contatos}"

    def exibir_contatos(self) -> None:
        saida = "Meus contatos: \n\n"
        
        for contato in self.__contatos:
            saida += str(contato)
            saida += "\n"
            
        print(saida)
        
def q3() -> None:
    intro(3)
    a1 = Agenda()
    
    a1.adicionar_contato(
        Contato(
            nome="Davi", 
            telefone=8899998888
        )
    )
    a1.adicionar_contato(
        Contato(
            nome="João", 
            telefone=8599888899
        )
    )
    a1.adicionar_contato(
        Contato(
            nome="Isabela", 
            telefone=1198988899
        )
    )
    
    a1.exibir_contatos()
    # print(a1)

    a1.remover_contato("Isabela")
    a1.exibir_contatos()


# Q4
class Carta:
    def __init__(self, valor: str, naipe: str):
        if isinstance(valor, int) and valor in [i for i in range(2, 11)]:
            valor = str(valor)
        
        if not isinstance(valor, (str)):
            raise TypeError("Erro! O valor da carta deve ser do tipo 'str'!")

        if not isinstance(naipe, str):
            raise TypeError("Erro! O naipe da carta deve ser do tipo 'str'!")

        valor = valor.upper()
        if valor not in Baralho.VALORES_VALIDOS:
            raise ValueError("Erro! O valor da carta deve ser: 'J', 'Q', 'K' ou 'A'!")

        naipe = naipe.upper()
        if not naipe in Baralho.NAIPES_VALIDOS:
            raise ValueError("Erro! Carta não possui naipe válido!")
        
        self.__valor = valor
        self.__naipe = naipe

    @property
    def valor(self):
        return self.__valor

    @property
    def naipe(self):
        return self.__naipe

    def __str__(self) -> str:
        if self.valor == "10":
            return f"{self.valor} | {self.naipe}"
        return f"{self.valor}  | {self.naipe}"

    # def __repr__(self) -> str:
    #     return self.__str__()
            

class Baralho:
    VALORES_VALIDOS: list[str] = [f"{i}" for i in range(2, 11)] + ["J", "Q", "K", "A"]
    NAIPES_VALIDOS: list[str] = ["COPAS", "ESPADAS", "OUROS", "PAUS"]
    
    def __init__(self):
        self.cartas: list[Carta] = [
            Carta(valor, naipe) for naipe in Baralho.NAIPES_VALIDOS for valor in Baralho.VALORES_VALIDOS
        ]

    def dar_carta(self) -> Carta:
        carta_retirada = self.cartas.pop()
        print("Uma carta foi retirada!")
        return carta_retirada

    def embaralhar(self) -> None:
        shuffle(self.cartas)
        print("Cartas embaralhadas!")

    def __mostrar(self) -> str:
        baralho = ""

        for carta in self.cartas:
            baralho += f"\n{carta}"

        return baralho
        
    def __str__(self) -> str:
        return f"Cartas do baralho: \n{self.__mostrar()}\n"
        
def q4() -> None:
    intro(4)
    b1 = Baralho()
    print(b1)
    b1.embaralhar()
    print(b1)

# Q5
class Aluno:
    def __init__(self, nome: str, idade: int, nota: float):
        self.__nome = nome
        self.__idade = idade
        self.__nota = nota

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f"Nome: {self.__nome} | Idade: {self.__idade} | Nota: {self.__nota}"

class Turma:
    def __init__(self):
        self.__alunos: list[Aluno] = []

    @property
    def alunos(self) -> list[Aluno]:
        return self.__alunos

    @alunos.setter
    def alunos(self, valor: list[Aluno]):
        if not isinstance(valor, list):
            raise TypeError()

        self.__alunos = valor
        
    def adicionar_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def remover_aluno(self, nome: str):
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.__alunos.remove(aluno)
                return

    def listar_alunos(self):
        saida = "Alunos: \n\n"
        
        for aluno in self.alunos:
           saida += f"{aluno}\n"
        
        print(saida)

def q5() -> None:
    intro(5)

    t1 = Turma()

    t1.adicionar_aluno(Aluno(nome="Davi", idade=20, nota=8.5))
    t1.adicionar_aluno(Aluno(nome="João", idade=18, nota=8.3))
    t1.adicionar_aluno(Aluno(nome="Alice", idade=21, nota=8.9))

    t1.listar_alunos()


    t1.remover_aluno("João")

    t1.listar_alunos()


# Q6
# Classe 'Produto' da questão 6
class ProdutoEstoque:
    def __init__(self, codigo, nome, preco, quantidade):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo
        
    def __str__(self) -> str:
        return f"Código: {self.codigo} | Nome: {self.__nome} | Preço: {self.__preco} | Quantidade: {self.__quantidade}"
        
class Estoque:
    def __init__(self):
        self.__produtos: list[ProdutoEstoque] = []

    # @property
    # def produtos(self) -> list[Produto]:
    #     return self.__produtos

    # @produtos.setter
    # if not isinstance(self.__produtos, list):
        # raise TypeError()
        
        # self.__produtos = 
    def adicionar_produto(self, produto: ProdutoEstoque) -> None:
        if not isinstance(produto, ProdutoEstoque):
            raise TypeError("Erro! O produto deve ser do tipo ProdutoEstoque!")
        self.__produtos.append(produto)

    def remover_produto(self, codigo) -> None:
        for produto in self.__produtos:
            if produto.codigo == codigo:
                self.__produtos.remove(produto)
                return

    def listar_produtos(self) -> None:
        saida = "Produtos: \n\n"
        
        for produto in self.__produtos:
           saida += f"{produto}\n"
           
        print(saida)

def q6() -> None:
    intro(6)

    e1 = Estoque()

    e1.adicionar_produto(
        ProdutoEstoque(
            codigo=1, 
            nome="Samsung Galaxy A55", 
            quantidade=9, 
            preco=1612.99
        )
    )
    e1.adicionar_produto(
        ProdutoEstoque(
            codigo=2, 
            nome="Iphone 17 Pro", 
            quantidade=15, 
            preco=5968
        )
    )
    
    e1.adicionar_produto(
        ProdutoEstoque(
            codigo=3, 
            nome="Samsung Galaxy S26", 
            quantidade=12, 
            preco=4809
        )
    )

    e1.listar_produtos()

    e1.remover_produto(1)

    e1.listar_produtos()
    fim()

# Q7
# Classe 'Produto' da questão 7
class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f"Código: {self.codigo} | Valor: {self.valor} | Descrição: {self.descricao}"


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int=0):
        self.__quantidade = quantidade
        self.produto = produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    def __str__(self):
        return f"Quantidade: {self.__quantidade} | Produto: {self.produto}"
    
class Pedido:
    quantidade_de_pedidos = 0
    def __init__(self):
        self.__valor_total: float = 0.0
        self.pedidos: list[ItemPedido] = []
        Pedido.quantidade_de_pedidos += 1
        self.__id = Pedido.quantidade_de_pedidos
        
    def adicionar_item(self, item: ItemPedido):
        if not isinstance(item, ItemPedido):
            raise TypeError()

        self.pedidos.append(item)

    def obter_total(self) -> float:
        valor_total = 0
        for pedido in self.pedidos:
            valor_total += pedido.quantidade * pedido.produto.valor

        self.__valor_total = valor_total
        return self.__valor_total
        
    def imprimir_pedido_completo(self):
        saida = f"Pedido Completo (id: {self.__id}): \n\n"

        saida += f"Valor total: R${self.obter_total():.2f}\n\n"
        saida += "Itens: \n\n"
        for pedido in self.pedidos:
            saida += f"{pedido}\n"
            
        print(saida)

def q7():
    intro(7)
    p1 = Pedido()

    p1.adicionar_item(
        ItemPedido(
            produto=Produto(100, 2200, "Lenovo Ideapad 3"),
            quantidade=12
        )
    )
    
    p1.adicionar_item(
        ItemPedido(
            produto=Produto(384, 55, "ff"), 
            quantidade=9
        )
    )

    p1.imprimir_pedido_completo()

    p2 = Pedido()

    p2.adicionar_item(
        ItemPedido(
            produto=Produto(1, 11, "aa"), 
            quantidade=12
        )
    )
    
    p2.adicionar_item(
        ItemPedido(
            produto=Produto(4, 55, "ff"), 
            quantidade=9
        )
    )

    p2.imprimir_pedido_completo()
    fim()

# Q8
class Carro:
    def __init__(self):
        self.__nome = "Carro"
        self.__posicao = 0
        velocidade_aleatoria = randint(1, 10)

        while velocidade_aleatoria in Corrida.velocidades_registradas:
            velocidade_aleatoria = randint(1, 10)
            
        self.__velocidade = velocidade_aleatoria
        Corrida.velocidades_registradas.append(self.__velocidade)

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def posicao(self) -> int:
        return self.__posicao

    @posicao.setter
    def posicao(self, valor: int) -> None:
        self.__posicao = valor
        
    @property
    def velocidade(self) -> int:
        return self.__velocidade
        
    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("Erro! nome deve ser texto!")

        self.__nome = valor
        
class Corrida:
    jogos: list[tuple["Corrida", str]] = []
    velocidades_registradas: list[int] = []
    
    def __init__(self):
        Corrida.velocidades_registradas = []
        self.__carros: list[Carro] = []
        self.__ganhador: Carro | None = None
        Corrida.jogos.append((self, ""))
        
    def adicionar_carro(self, carro: Carro) -> "Corrida":
        if not isinstance(carro, Carro):
            raise TypeError()

        carro.nome += f" {len(self.__carros) + 1}"
        self.__carros.append(carro)
        return self

    def gerar_carros(self, quantidade: int) -> "Corrida":
        """
        Ao todo, adicione no máximo 10 carros
        """
        for i in range(quantidade):
            self.adicionar_carro(Carro())

        if len(self.__carros) > 10:
            raise ValueError("A corrida pode ter no máximo 10 carros!")
            
        return self
        
    def iniciar(self) -> "Corrida":
        esp = len(str(len(self.__carros)))
        espaco = " " * esp
        
        self.__ganhador = None
        
        estado_da_corrida = ""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        while True:
            estado_da_corrida = ""
            for i, carro in enumerate(self.__carros):
                evolucao = ""
                
                carro.posicao += carro.velocidade
                evolucao = "#" * carro.posicao

                espaco = " " * (esp - len(str(i + 1)))

                estado_da_corrida += f"{carro.nome}{espaco}: {evolucao}\n"
                
                print(f"{carro.nome}{espaco}: {evolucao}")
                
                if not self.__ganhador and len(evolucao) >= 50:
                    self.__ganhador = carro

            sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
                
            if self.__ganhador:
                os.system('cls' if os.name == 'nt' else 'clear')
                Corrida.jogos[len(Corrida.jogos) - 1] = (self, estado_da_corrida)
                
                if self is Corrida.jogos[len(Corrida.jogos) - 1][0]:
                    for i, jogo in enumerate(Corrida.jogos):
                        print(Corrida.jogos[i][1])

                    for i, jogo in enumerate(Corrida.jogos):
                        jogo[0].__exibir_resultado(i + 1)
                else:
                    sleep(1)
                    
                return self
            
            
    def __exibir_resultado(self, num: int) -> None:
        if isinstance(self.__ganhador, Carro):
            print("\nCorrida encerrada!")
            print(f"{self.__ganhador.nome} ganhou a corrida {num}! \n")
            return
            
        print("Erro! Não houve ganhador!")

def q8():
    intro(8)
    jogo_1 = Corrida()
    
    (jogo_1
        .gerar_carros(10)
        .iniciar()
    )

    jogo_2 = Corrida()
    
    (jogo_2
        .gerar_carros(3)
        .iniciar()
    )
# ----------------------------------------------------------------------------------------
    
# ----------------------------------------------------------------------------------------
# Chamada de cada questão:     
if __name__ == "__main__":
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
   #q8()
# ----------------------------------------------------------------------------------------