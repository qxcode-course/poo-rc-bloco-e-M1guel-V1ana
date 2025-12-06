from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, area, perimetro, nome ):
        self.area = area
        self.perimetro = perimetro
        self.nome = nome

    def getArea(self):
        return self.area
    def getPerimeter(self):
        return  self.perimetro
    def getName(self):
        return self.nome


class Point2D():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle(Shape):
    def __init__(self, ):