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

    @abstractmethod
    def mover(self): # me retorna vazio, por hora irei fazer assim, pois achei mais simples ( por hora)
       pass

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()


class Zebra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")

    def fazer_som(self):
        return "a zebra faz zurro!"

    def mover(self):
        return ("Zebra está correndo: pocotó pocotó")


class Lobo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>!")

    def fazer_som(self):
        return "A-woooooooooo!"

    def mover(self):
        return "tum-tum... tum-tum"



class Pato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        print(f"Eu sou um(a) <{self.getNome()}>")

    def fazer_som(self):
        return "Quack!"

    def mover(self):
        return "squish squish"



animais: list[Animal] = [Zebra("Zebra"), Lobo("Lobo"), Pato("Patin")]

for animal in animais:
    animal.apresentar_nome()
    print(animal.mover())
    print(animal.fazer_som())