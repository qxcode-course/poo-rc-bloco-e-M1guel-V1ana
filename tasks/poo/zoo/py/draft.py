from abc import ABC, abstractmethod
# importando o modulo abc para definição de classes abstratas


#Criação de uma classe abstrata.
class Animal(ABC):
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    @abstractmethod
    #def apresetar_nome(self):
    #   pass  #  metodo sem orientação

    def apresentar_nome(self):
        pass





class Zebra(Animal):
    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")



class Lobo(Animal):
    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")



class Pato(Animal):
    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>")


animais: list[any] = [Zebra("Mico"), Lobo("Alfred"), Pato("Geraldinho")]

for animal in animais:
    animal.apresentar_nome()