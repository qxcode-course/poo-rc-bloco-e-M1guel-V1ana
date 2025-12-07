from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, hora_entrada: int ):
        self.id = id
        self.tipo = tipo
        self.entrada = hora_entrada




    def setEntrada(self, entrada: int):
        self.entrada = entrada

    def getEntrada(self):
        return self.entrada
