class Drone:
    def __init__(self, x=0, y=0, altura=0):
        self.__x = x
        self.__y = y
        self.__altura = altura

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, valor):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        pass

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        pass
    
    def voar(self, deslocamento_z: int | float):
        if not isinstance(deslocamento_z, (int, float)):
            raise TypeError("O deslocamento vertical deve ser um número!")
        
        nova_altura = self.altura + deslocamento_z
        
        if nova_altura < 0 or nova_altura > 120:
            raise ValueError("A nova altura deve estar entre 0 e 120 metros!")

        self.__altura = nova_altura

    def mover(self, deslocamento_x: int | float, deslocamento_y: int | float):
        deslocamento_x_e_numero = isinstance(deslocamento_x, (int, float))

        deslocamento_y_e_numero = isinstance(deslocamento_y, (int, float))

        if not deslocamento_x_e_numero or not deslocamento_y_e_numero:
            raise TypeError("O deslocamento horizontal deve ser um número!")

        if self.altura <= 0:
            raise RuntimeError("Impossível mover, pois o drone está no chão!")
        
        self.__x += deslocamento_x
        self.__y += deslocamento_y

    
    def __str__(self):
        return f"Drone em ({self.x}, {self.y}) - Altura: {self.altura} m"
    

if __name__ == "__main__":
    d1 = Drone()

    # # ValueError (voar) (altura > 120)
    try:
        d1.voar(150)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)


    d2 = Drone(1, 5, 10)

    # # ValueError (voar) (altura < 0)
    try:
        d2.voar(-30000)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    
    # # Caso de sucesso (voar):
    d3 = Drone(2, 23, 45)

    print(d3)

    try:
        d3.voar(20)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    
    print(d3)


    d4 = Drone(10, 20, 21)

    # # TypeError (mover) (deslocamento_x e deslocamento_y devem ser int ou float)
    try:
        d4.mover("dez", "cinco")
    except TypeError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    

    d5 = Drone(10, 20)
    # # RuntimeError (mover) (altura = 0, drone no chão)
    try:
        d5.mover(14, 54)
    except TypeError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    
    
    d6 = Drone(12, 31, 5)

    # # Caso de sucesso (mover): 
    print(d6)

    try:
        d6.mover(10, 20)
    except TypeError as e:
        print(e)
    except RuntimeError as e:
        print(e)

    print(d6)
     