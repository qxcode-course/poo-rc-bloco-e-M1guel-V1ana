from abc import ABC, abstractmethod
# importando o modulo abc para definição de classes abstratas

#Criação de uma classe abstrata.
class Animal(ABC):
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    @abstractmethod
    def apresentar_nome(self) -> str:
        pass

    @abstractmethod
    def fazer_som(self) ->str:
        pass

    @abstractmethod
    def mover(self) ->str: # me retorna vazio, por hora irei fazer assim, pois achei mais simples ( por hora)
       pass

def apresentar(animal: Animal):
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())

class Zebra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>!"

    def fazer_som(self):
        return "a zebra faz zurro!"

    def mover(self):
        return ("Zebra está correndo: pocotó pocotó")


class Lobo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>!"

    def fazer_som(self):
        return "A-woooooooooo!"

    def mover(self):
        return "O lobo anda silenciosamente pela neve..."



class Pato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>"

    def fazer_som(self):
        return "Quack!"

    def mover(self):
        return "o pato nada no lago"


class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self) -> str:
        return f"Eu sou um(a) <{self.getNome()}>"

    def fazer_som(self) ->str:
        return "au au"
    def mover(self) ->str:
        return "o cachorro pede carinho ao dono"

class Dragao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self) -> str:
        return f"Eu sou um(a) <{self.getNome()}> "

    def fazer_som(self) ->str:
        return "Rawr / Rwar"

    def mover(self) ->str:
        return "O dragão bate as asas e voa"

animais: list[Animal] = [Zebra("Zebra"), Lobo("Lobo"), Pato("Patin"), Cachorro("Cachorro"), Dragao("Dragão")]

for animal in animais:
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())