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

    def setEntrada(self, hora: int) -> None:
        self.horaEntrada = hora

    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        return f"{self.tipo}: {self.id} : {self.horaEntrada}"


class Bike(Veiculo):
    def __str__(self, id, tipo, horaEntrada):
        super().__str__(id, tipo, horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        return 3.00


class Moto(Veiculo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        return tempo / 20

class Carro(Veiculo):
    def __init__(self, id, tipo, horaEntrada):
        super().__init__(id, tipo, horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10
        if valor > 5:
            return f"{valor:.2f}"
        else:
            return f"{5:.2f}"


class Estacionamento:
    def __init__(self, horaAtual: int = 0):
        self.veiculos: list[Veiculo] = []
        self. horaAtual = horaAtual

    def procucarVeiculo(self, id: str):


    def estacionar(self, veiculo: Veiculo) -> None :
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)
    def pagar(self, id: str) -> None:
        pos = self.procurarVeiculo(id)
        if pos == -1:
            print("veiculo não encontrado")
            return

        veiculo = self.veiculos[pos]
        valor = veiculo.calcularValor(self.horaAtual)
        print(f" Valor a pagar: R$ {valor:.2f}")

    def sair(self, id: str):
        pos = self.procurarVeiculo(id)
        if pos == -1:
            print("Veiculo não encontrado")
            return

        veiculo = self.veiculos[pos]
        valor = veiculo.calcularValor(self.horaAtual)
        print(f"veiculo: {id} saiu. Valor pago: R$: {valor:.2f}")
    def passarTempo(self, tempo: int) -> None:
        self.horaAtual += tempo

    def __str__(self):
        veiculos = "\n". join(str(x) for x in self.veiculos)

def main():
    estacionar = Estacionamento()

    while True:

        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionar)

        elif args[0] == "tempo":
            estacionar.passarTempo(int(args[1]))
        else:
            print("fail: comando invalido!!!")
main()