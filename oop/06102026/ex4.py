class Veiculo:
    def __init__(self, marca, km_rodado, numero_chassi):
        self.marca = marca
        self._km_rodado = km_rodado
        self._numero_chassi = numero_chassi


class Carro(Veiculo):
    def detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Km rodado: {self._km_rodado}")
        print(f"Número de chassi: {self._numero_chassi}")


c1 = Carro("fff", 20000, 2393)
c2 = Carro("fiat", 2321, 9939)

c1.detalhes()
c2.detalhes()