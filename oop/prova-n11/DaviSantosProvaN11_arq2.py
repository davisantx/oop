from DaviSantosProvaN11_arq1 import Drone

drone = Drone()

def entrada(min: int, max: int, mensagem: str="") -> int:
    valor = int(input(mensagem))
    print()

    if not isinstance(valor, int):
        raise TypeError("Opção inválida! Insira um número inteiro!")

    if valor < min or valor > max:
        raise ValueError("Opção inválida! Apenas números de 1 a 3!")

    return valor

def opcao_voar(drone: Drone) -> bool:
    try:
        print(f"Informações atuais acerca do drone: {drone}\n")
        drone.voar(float(input("Insira o Deslocamento z: ")))
    except TypeError as e:
        print()
        print(e)
        print("\nTente novamente!\n")
        return False
    except ValueError as e:
        print()
        print(e)
        print("\nTente novamente!\n")
        return False

    print("\nDrone voou com sucesso!")
    print(f"Informações atuais do drone após o voo: {drone}\n")
    return True

def opcao_mover(drone: Drone) -> bool:
    try:
        print(f"Informações atuais acerca do drone: {drone}\n")
        drone.mover(float(input("Insira o Deslocamento x: ")), float(input("Insira o Deslocamento y: ")))
    except RuntimeError as e:
        print()
        print(e)
        print("\nTente novamente!\n")
        return False
    except ValueError as e:
        print()
        print(e)
        print("\nTente novamente!\n")
        return False

    print("\nDrone moveu com sucesso!")
    print(f"Drone após mover: {drone}\n")
    return True


if __name__ == "__main__":
    while True:
        print("SISTEMA DE CONTROLE DE DRONE \n")
        print("1 - Voar")
        print("2 - Mover")
        print("3 - Sair")

        opcao = 0

        try:
            opcao = entrada(min=1, max=3, mensagem="\nOpção: ")
        except TypeError as e:
            print(e)
            continue
        except ValueError as e:
            print(e)
            continue

        if opcao == 1:
            opcao_voar(drone)
        elif opcao == 2:
            opcao_mover(drone)
        elif opcao == 3:
            print("\nSaindo do sistema...")
            exit()
        