from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        return self.area
    @abstractmethod
    def getPerimeter(self):
        return  self.perimetro
    @abstractmethod
    def getName(self):
        return self.nome


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Circle(Shape):
    def __init__(self, area, perimetro, nome, center: Point2D, name: str = "Circ", radius: float):
        super().__init__(area, perimetro, nome)
        self.name = name
        self.center = center
        self.radius = radius

    def getName(self):
        return self.name

    def getArea(self):
        return math.pi * (self.radius**2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f"{self.name}: C=({self.center}), R={self.radius}"


class Rectangle(Shape):
    def __init__(self, area, perimetro, nome, name: str = "Rect", p1: Point2D, p2:Point2D):
        super().__init__(area, perimetro, nome)
        self.name = name
        self.p1 = p1
        self.p2 = p2

    def getName(self):
        return self.name

    def getArea(self):
        largura = abs(self.p2.x - self.p1.x)
        altura = abs(self.p2.y - self.p1.y)
        return largura * altura

    def getPerimeter(self):
        largura = abs(self.p2.x - self.p1.x)
        altura = abs(self.p2.y - self.p1.y)
        return 2 * (largura + altura)

    def __str__(self):
        return f"{self.name}: P1={self.p1} P2={self.p2}"


