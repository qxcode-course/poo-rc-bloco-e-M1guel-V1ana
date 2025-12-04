from abc import ABC, abstractmethod
# importando o modulo abc para definição de classes abstratas


#Criação de uma classe abstrata.
class Animal(ABC):
    def __init__(self, nome: str):
        self.__nome = nome

    @abstractmethod
    #def apresetar_nome(self):
    #   pass  //  metodo sem orientação

    def apresentar_nome(self):
        pass





class Zebra(Animal):





#animais: list[any] = []

#for animais in Animal:
#   ...