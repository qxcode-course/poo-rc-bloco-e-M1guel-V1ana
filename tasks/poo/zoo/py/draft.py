from abc import ABC, abstractmethod
# importando o modulo abc para definição de classes abstratas


#Criação de uma classe abstrata.
class Animal(ABC):
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    @abstractmethod
    def apresentar_nome(self):
        pass

    @abstractmethod
    def fazer_som(self):
        pass





class Zebra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")

    def fazer_som(self):
        return "a zebra faz zurro!"


class Lobo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")

    def fazer_som(self):
        return "o lobo faz auuuuuu!"



class Pato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)
    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>")

    def fazer_som(self):
        return "o pato faz Quack!"


animais: list[any] = [Zebra("Zebra"), Lobo("Lobo"), Pato("Patin")]

for animal in animais:
    animal.apresentar_nome()
    print(animal.fazer_som())