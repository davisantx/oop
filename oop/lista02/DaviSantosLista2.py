from typing import Final

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
# Q1
class Livro:
    def __init__(self, titulo: str, autor: str, total_paginas: int, pagina_atual: int):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas

        if self.total_paginas < 0:
            self.total_paginas = 0

        self.pagina_atual = pagina_atual

        if self.pagina_atual < 0:
            self.pagina_atual = 0

    def __verificar_se_pagina_existe(self, pagina: int):
        return pagina >= 0 and pagina <= self.total_paginas
        
    def avancar_pagina(self):
        pagina_atual = self.pagina_atual + 1
        if not self.__verificar_se_pagina_existe(pagina_atual):
            return
        self.pagina_atual = pagina_atual

    def voltar_pagina(self):
        pagina_atual = self.pagina_atual - 1
        if not self.__verificar_se_pagina_existe(pagina_atual):
            return
        self.pagina_atual = pagina_atual

    def ir_para_pagina(self, nova_pagina: int):
        if not self.__verificar_se_pagina_existe(nova_pagina):
            return
        self.pagina_atual = nova_pagina

    def __str__(self):
        return f"""
        Título: {self.titulo}
        Autor: {self.autor}
        Total páginas: {self.total_paginas}
        Página atual: {self.pagina_atual}
        """

def q1():
    print("QUESTÃO 1\n\n")
    l1 = Livro(
        titulo="O Alienista", 
        autor="Machado de Assis", 
        total_paginas=134, 
        pagina_atual=19
    )

    l2 = Livro(
        titulo="O Cortiço",
        autor="Aluísio Azevedo",
        total_paginas=211,
        pagina_atual=43
    )

    # l1
    print(l1)
    
    for i in range(5):
        l1.avancar_pagina()
        
    print(l1)
    
    l1.voltar_pagina()
    
    print(l1)

    # l2
    print(l2)
    
    for i in range(2):
        l1.avancar_pagina()
        
    print(l2)

    for i in range(4):
        l2.voltar_pagina()
        
    print(l2)

    print("\n\n")

# Q2
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds >= 59:
            self.minutes += 1
            self.seconds = 0
        return

        self.seconds += 1

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"


def q2():
    print("QUESTÃO 2\n\n")
    stp = Stopwatch()
    
    for i in range(70):
        stp.tick()
        print(stp)

    print("\n\n")

# Q3
class Clock:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        self.seconds += 1
                
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                
                if self.hours == 24:
                    self.hours = 0

    def set(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    

def q3():
    print("QUESTÃO 3\n\n")
    
    clock = Clock(23, 59, 55)
    print(clock)

    for i in range(6):
        clock.tick()
        print(clock)
    
    clock.set(12, 5)
    print(clock)
    
    print("\n\n")

# Q4
class LunchCard0:
    def __init__(self, saldo: float):
        if saldo < 0:
            self.saldo = 0
            return
        self.saldo = saldo

    def __str__(self):
        return f"The balance is {self.saldo:.1f} euros"

    def _verificar_se_saldo_e_valido(self):
        return self.saldo >= 0
    
    def eat_lunch(self):
        if not self._verificar_se_saldo_e_valido():
            self.saldo = 0
            return
        self.saldo -= 2.60

    def eat_special(self):
        if not self._verificar_se_saldo_e_valido():
            self.saldo = 0
            return
        self.saldo -= 4.60

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("Amount is invalid: never minor then zero!")
        self.saldo += amount


def q4():
    print("QUESTÃO 4\n\n")
    peter_card = LunchCard0(20)
    grace_card = LunchCard0(30)

    peter_card.eat_special()
    grace_card.eat_lunch()

    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    peter_card.deposit_money(20)

    grace_card.eat_special()

    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    for i in range(2):
        peter_card.eat_lunch()

    grace_card.deposit_money(50)

    print(f"Peter: {peter_card}")
    print(f"Grace: {grace_card}")

    print("\n\n")

# Q5
class LunchCard:
    """
    Versão melhorada do LunchCard0 da questão anterior
    """

    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance - amount < 0:
            return False

        self.balance -= amount
        return True


class PaymentError(Exception):
    pass

class DepositError(Exception):
    pass

class PaymentTerminal:
    LUNCH_PRICE: Final[float] = 2.50
    SPECIAL_PRICE: Final[float] = 4.30

    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float) -> float:
        if payment < 0:
            raise ValueError("Value Error: Payment must be positive value (> 0)")
        
        if payment < PaymentTerminal.LUNCH_PRICE:
            raise PaymentError(f"Payment Error: Lunch price is {PaymentTerminal.LUNCH_PRICE}!")

        self.funds += PaymentTerminal.LUNCH_PRICE
        self.lunches += 1
        
        troco = payment - PaymentTerminal.LUNCH_PRICE
        return troco

    def eat_special(self, payment: float) -> float:
        if payment < 0:
            raise ValueError("Value Error: Payment must be positive value (> 0)")
 
        if payment < PaymentTerminal.SPECIAL_PRICE:
            raise PaymentError('Payment Error: Lunch price is 4.30')
              
        self.funds += PaymentTerminal.SPECIAL_PRICE

        self.specials += 1

        troco = payment - PaymentTerminal.SPECIAL_PRICE
        return troco

    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        if card.subtract_from_balance(PaymentTerminal.LUNCH_PRICE):
            self.lunches += 1
            return True

        return False

    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        if card.subtract_from_balance(PaymentTerminal.SPECIAL_PRICE):
            self.specials += 1
            return True

        return False
        
    def deposit_money_on_card(self, card: LunchCard, sum: float):
        if sum < 0:
            raise ValueError("Value Error: is impossible deposit negative value of money!")
            return
        
        card.deposit_money(sum)
        self.funds += sum

def q5():
    print("QUESTÃO 5\n\n")
    def p1():
        print("Q5 - Parte 1: \n")
        
        card = LunchCard(10)
        print("Balance", card.balance)
        result = card.subtract_from_balance(8)
        print("Payment successful:", result)
        print("Balance", card.balance)
        result = card.subtract_from_balance(4)
        print("Payment successful:", result)
        print("Balance", card.balance)
    
        print("\n\n")

    def p2():
        print("Q5 - Parte 2: \n")
        exactum = PaymentTerminal()
        change = exactum.eat_lunch(10)
        print("The change returned was", change)
        change = exactum.eat_lunch(5)
        print("The change returned was", change)
        change = exactum.eat_special(4.3)
        print("The change returned was", change)
        print("Funds available at the terminal:", exactum.funds)
        print("Regular lunches sold:", exactum.lunches)
        print("Special lunches sold:", exactum.specials)

        print("\n\n")

    def p3():
        print("Q5 - Parte 3: \n")
        
        exactum = PaymentTerminal()
        change = exactum.eat_lunch(10)
        print("The change returned was", change)
        card = LunchCard(7)
        result = exactum.eat_special_lunchcard(card)
        print("Payment successful:", result)
        result = exactum.eat_special_lunchcard(card)
        print("Payment successful:", result)
        result = exactum.eat_lunch_lunchcard(card)
        print("Payment successful:", result)
        print("Funds available at the terminal:", exactum.funds)
        print("Regular lunches sold:", exactum.lunches)
        print("Special lunches sold:", exactum.specials)

        print("\n\n")
        
    def p4():
        print("Q5 - Parte 4: \n")

        exactum = PaymentTerminal()
        card = LunchCard(2)
        print(f"Card balance is {card.balance} euros")
        result = exactum.eat_special_lunchcard(card)
        print("Payment successful:", result)
        exactum.deposit_money_on_card(card, 100)
        print(f"Card balance is {card.balance} euros")
        result = exactum.eat_special_lunchcard(card)
        print("Payment successful:", result)
        print(f"Card balance is {card.balance} euros")
        print("Funds available at the terminal:", exactum.funds)
        print("Regular lunches sold:", exactum.lunches)
        print("Special lunches sold:", exactum.specials)

    # Execução de cada uma das partes da questão
    p1()
    p2()
    p3()
    p4()

    print("\n\n")


# Q6
class Personagem:
    def __init__(self, nome: str, vida: int = 100, ataque: int = 10, nivel: int = 1):
        self.__nome = nome
        self.__vida = vida
        self.__ataque = ataque
        self.__nivel = nivel

    def atacar(self, inimigo: "Personagem"):
        print(f"{self.__nome} atacou {inimigo.__nome} causando {self.__ataque} de dano!")
        inimigo.__receber_dano(self.__ataque)

        
    def __receber_dano(self, dano: int):
        if self.__vida > dano:
            self.__vida -= dano
            print(f"{self.__nome} agora tem {self.__vida} de vida.")
            return

        print(f"{self.__nome} sofreu dano e foi derrotado!")
        self.__vida = 0
        
    def subir_nivel(self):
        self.__nivel += 1
        self.__ataque += 5
        self.__vida += 20
        
        print(f"{self.__nome} subu para o nível {self.__nivel}! Ataque aumentado para {self.__ataque}, Vida agora é {self.__vida}")

    def __str__(self):
        return f"Nome: {self.__nome} | Nível: {self.__nivel} | Vida: {self.__vida} | Ataque: {self.__ataque}"

    

def q6():
    print("QUESTÃO 6\n\n")
    rockeiro = Personagem("Rockeiro", ataque=12, vida=120)
    pirangueiro = Personagem("Pirangueiro", ataque=15, vida=150)

    rockeiro.atacar(pirangueiro)
    pirangueiro.atacar(rockeiro)

    rockeiro.subir_nivel()
    print(rockeiro)


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# Chamada de cada questão:     
q1()
q2()
q3()
q4()
q5()
q6()
# ----------------------------------------------------------------------------------------