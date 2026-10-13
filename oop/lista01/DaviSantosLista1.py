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
# Questões:
# 
# Classe 'Livro'
class Livro:
    def __init__(self, nome: str, autor: str, genero: str, ano: int):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano
    
    def obter_detalhes(self) -> str:
        return f"""
            Nome do livro: {self.nome},
            Nome do autor: {self.autor},
            Gênero do livro: {self.genero}
            Ano do livro: {self.ano}
        """

# Classe 'Pessoa'
class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def retorna_primeiro_nome(self):
        return self.nome.strip().split(" ")[0]

    def retorna_ultimo_nome(self):
        nome = self.nome.strip().split(" ")
        return nome[len(nome) - 1]


# Classe 'Carro'
class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, velocidade_atual: float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

        if velocidade_atual >= 0:
            self.velocidade_atual = velocidade_atual
        else:
            self.velocidade_atual = 0

    def acelerar(self):
        velocidade_antiga = self.velocidade_atual
        self.velocidade_atual += 10

        print(f"{self.modelo} acelerou! {velocidade_antiga}km/h -> {self.velocidade_atual}km/h")

    def frear(self):
        velocidade_antiga = self.velocidade_atual
        
        if self.velocidade_atual < 10:
            self.velocidade_atual = 0
        self.velocidade_atual -= 10

        print(f"{self.modelo} freou! {velocidade_antiga}km/h -> {self.velocidade_atual}km/h")

    def pintar(self, nova_cor: str):
        cor_antiga = self.cor
        self.cor = nova_cor
        
        print(f"{self.modelo} teve sua cor trocada de {cor_antiga} para {self.cor}")

    def mostrar_informacoes(self):
        return f"""
            Marca: {self.marca}
            Modelo: {self.modelo}
            Ano: {self.ano}
            Cor: {self.cor}
            Velocidade atual: {self.velocidade_atual}
        """
        

# Q2 -> Função que auxilia a função principal
def exibir_detalhes_do_livro(livro: Livro, numero_livro: int) -> None:
    saida = ""
    saida += f"Detalhes do Livro {numero_livro}: {livro.nome}: \n\n"
    saida += f"{livro.obter_detalhes()}\n"

    print(saida)

# Q2 -> Função principal
def livro_mais_antigo(livro1: Livro, livro2: Livro) -> None:
    if livro1.ano == livro2.ano:
        print(f"Entre '{livro1.nome}' e '{livro2.nome}'")
        print("Ambos os livros foram feitos no mesmo ano!\n")
        exibir_detalhes_do_livro(livro1, 1)
        exibir_detalhes_do_livro(livro2, 2)
        return
    
    if livro1.ano < livro2.ano:
        print(f"Entre '{livro1.nome}' e '{livro2.nome}', o livro mais antigo é o: '{livro1.nome}'\n")
        exibir_detalhes_do_livro(livro1, 1)
        return

    if livro2.ano < livro1.ano:
        print(f"Entre '{livro1.nome}' e '{livro2.nome}', o livro mais antigo é o: '{livro2.nome}'\n")
        exibir_detalhes_do_livro(livro2, 2)
        return



# Q3 -> Função principal
def livros_do_genero(livros: list[Livro], genero: str) -> list[Livro]:
    return [livro for livro in livros if livro.genero == genero]

# Q3 -> Função auxiliar
def exibir_os_detalhes_dos_livros(livros: list[Livro]) -> None:
    for i in range(len(livros)):
        exibir_detalhes_do_livro(livros[i], i + 1)

# Q4 -> Função auxiliar
def exibir_primeiro_e_ultimo_nome(pessoa: Pessoa) -> None:
    saida = ""
    primeiro_nome = pessoa.retorna_primeiro_nome()
    ultimo_nome = pessoa.retorna_ultimo_nome()
    
    saida += f"Primeiro nome de '{pessoa.nome}': {primeiro_nome}\n"
    saida += f"Último nome de '{pessoa.nome}': {ultimo_nome}\n"

    print(saida)
    
# Livros (pseudo-ficticios)
dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "romance", 1899)
o_hobbit = Livro("O Hobbit", "J.R.R. Tolkien", "fantasia", 1937)

livro_teste_1 = Livro("Grande Sertão Veredas", "João Guimarães Rosa", "aventura", 1999)
livro_teste_2 = Livro("O Quinze", "Raquel de Queiroz", "historia", 1999)

livro_teste_3 = Livro("O Ateneu", "Raul Pompeia", "romance", 1839)
livro_teste_4 = Livro("Morte e Vida Severina", "João Cabral de Melo Neto", "fantasia", 1994)
livro_teste_5 = livro_teste_2 = Livro("Os Sertões", "Euclides da Cunha", "historia", 1912)

livros = [dom_casmurro, o_hobbit, livro_teste_1, livro_teste_2, livro_teste_3, livro_teste_4]


# Q1 -> Exibir

def q1():
    print("Q1 - INFORMAÇÕES BÁSICAS SOBRE O LIVRO\n")
    print(f"{dom_casmurro.autor}: {dom_casmurro.nome} ({dom_casmurro.ano})")
    print(f"O gênero do livro {o_hobbit.nome} é {o_hobbit.genero}")
    print("\n\n\n")

#Q2 -> Exibir


def q2():
    print("Q2 - DETALHES DO LIVRO MAIS ANTIGO\n") 
    livro_mais_antigo(dom_casmurro, o_hobbit)
    livro_mais_antigo(livro_teste_1, livro_teste_2)
    livro_mais_antigo(livro_teste_2, livro_teste_1)
    livro_mais_antigo(o_hobbit, dom_casmurro)
    print("\n\n\n")

#Q3 -> Exibir

def q3():
    print("Q3 - LIVROS DO GÊNERO...\n")
    romances = livros_do_genero(livros, "romance")
    fantasias = livros_do_genero(livros, "fantasia")
    historias = livros_do_genero(livros, "historia")
    
    print("Livros de romance: \n")
    exibir_os_detalhes_dos_livros(romances)
    
    print("Livros de fantasia: \n")
    exibir_os_detalhes_dos_livros(fantasias)
    
    print("Livros de historia: \n")
    exibir_os_detalhes_dos_livros(historias)
    
    print("\n\n")


# Pessoas

julia = Pessoa("Julia Barros Carneiro")
alice = Pessoa("Alice Santos Costa")
pedro = Pessoa("Pedro Cavalcante Neto")
patrick = Pessoa("Patrick Silva Carvalho")

#Q4 -> Exibir

def q4():
    print("Q4 - PESSOA...\n")
    exibir_primeiro_e_ultimo_nome(julia)
    
    exibir_primeiro_e_ultimo_nome(alice)
    exibir_primeiro_e_ultimo_nome(pedro)
    exibir_primeiro_e_ultimo_nome(patrick)
    print("\n\n\n")


# Carros

c1 = Carro("Chevrolet", "Cruze LT", 2019, "vermelho", 60)
c2 = Carro("Fiat", "Palio", 2010, "prata", 32)
c3 = Carro("Toyota", "Corolla Cross", 2023, "prata", 83)

#Q5 -> Exibir

def q5():
    print("Q5 - CARRO...\n")
    
    # c1
    c1.acelerar()
    c1.frear()
    
    
    #c2
    for i in range(3):
        c2.acelerar()
        
    c2.frear()
    
    #c3
    for i in range(4):
        c3.frear()
    
    c3.acelerar()
    
    print("\n\n\n")

# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Chamada de cada questão:     
q1()
q2()
q3()
q4()
q5()
# ----------------------------------------------------------------------------------------