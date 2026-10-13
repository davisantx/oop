class Equipamento:
    def ligar(self):
        print("Ligando...")

class Impressora(Equipamento):
    def __init__(self):
        pass
        
    def ligar(self):
        print("Ligando Impressora")

    def imprimir(self, texto: str):
        print(f"Imprimindo: {texto}")
        
class Scanner(Equipamento):
    def ligar(self):
        print("Ligando Scanner")
        
    def digitalizar(self):
        print("Digitalizando")
  
class MultiFuncional(Impressora, Scanner):
    def __init__(self):
        pass