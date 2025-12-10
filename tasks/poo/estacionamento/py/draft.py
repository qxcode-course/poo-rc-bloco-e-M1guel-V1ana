from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaentrada: float):
        self.id = id
        self.tipo = tipo
        self.horaentrada = horaentrada

    def setEntrada(self, hora: int):
        self.horaentrada = hora

    def getEntrada(self):
        return self.horaentrada
    def getTipo(self):
        return self.tipo
    def getId(self):
        return self.id

    def __str__(self):
        return f"{self.tipo}: {self.id}: {self.horaentrada}}"


    @abstractmethod
    def calcHorasaida(self, horasaida: int):
        pass



class Bike(Veiculo):
    def __init__(self, id, tipo, horaentrada):
        super().__init__(id, tipo, horaentrada)

    def calcHorasaida(self, horasaida: float) -> float:
        return 3.00

class Moto(Veiculo):
    def __init__(self, id, tipo, horaentrada):
        super.__init__(id, tipo, horaentrada)

    def calcHorasaida(self, horasaida: int) -> float:
        valor = self.horaentrada / 20
        return valor


class Carro(Veiculo):
    def __init__(self, id, tipo, horaentrada):
        super().__init__(id, tipo, horaentrada)

    def calcHorasaida(self, horasaida: int) -> float:
        valor =