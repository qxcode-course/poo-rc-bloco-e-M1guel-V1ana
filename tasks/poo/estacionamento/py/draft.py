from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.horaEntrada
    def getTipo(self) -> str:
        return self.tipo
    def getId(self) -> str:
        return self.id

    def sethoraEntrada(self, hora: int) -> None:
        self.horaEntrada = hora

    @abstractmethod
    def calcularHorasaida(self, horaSaida: int):
        pass

    def __str__(self):
        return f"{self.id}: {self.tipo} : {self.horaEntrada}"





class Bike(Veiculo):
    def __init__(self):










def main():
    estacionar: list[Estacionamento] = []


    while True:

        line = input()
        print("$" + line)
        args: list[args] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "show":
            print(estacionar)

main()