from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = None

    def getEntrada(self) -> int:
        return self.horaEntrada
    def getTipo(self) -> str:
        return self.tipo
    def getId(self) -> str:
        return self.id

    def setEntrada(self, hora: int) -> None:
        self.horaEntrada = hora

    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        return f"{self.tipo}: {self.id} : {self.horaEntrada}"


class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")
    def calcularValor(self, horaSaida: int) -> float:
        return 3.0


class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        return tempo / 20

class Carro(Veiculo):
    def __init__(self, id: str):
        super.__init__(id, "Carro")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10
        return max(valor, 5.0)


class Estacionamento:
    def __init__(self, horaAtual: int):
        self.horaAtual = horaAtual
        self.veiculos: list[Veiculo] = []

    def procurarVeiculo

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