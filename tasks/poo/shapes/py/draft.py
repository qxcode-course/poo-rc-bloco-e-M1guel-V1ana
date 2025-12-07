from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass
    @abstractmethod
    def getPerimeter(self):
        pass
    @abstractmethod
    def getName(self):
        pass


def info(shape: Shape):
    name  = shape.getName()
    area = shape.getArea()
    perimeter = shape.getPerimeter()
    return f"{name}: A={area:.2f} P={perimeter:.2f}"

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Circle(Shape):
    def __init__(self,center: Point2D, radius: float, name: str = "Circ"):
        self.center = center
        self.radius = radius
        self.name = name


    def getName(self):
        return self.name

    def getArea(self):
        return math.pi * (self.radius**2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return f"{self.name}: C={self.center}, R={self.radius:.2f}"


class Rectangle(Shape):
    def __init__(self,p1: Point2D, p2:Point2D,):
        self.name = "Rect"
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



def main():
    forms: list[Shape] = []

    while True:
        try:
            line = input()
            print("$" + line)
            args: list[str] = line.split(" ")

            if args[0] == "end":
                break
            elif args[0] == "circle":
                x = float(args[1])
                y = float(args[2])
                r = float(args[3])
                center = Point2D(x,y)
                circle = Circle(center, r)
                forms.append(circle)
            elif args[0] == "show":
                for shape in forms:
                    print(shape)
            elif args[0] == "rect":
                p1 = Point2D(float(args[1]), float(args[2]))
                p2 = Point2D(float(args[3]), float(args[4]))
                rect = Rectangle(p1, p2)
                forms.append(rect)

            elif args[0] == "info":
                for shape in forms:
                    print(info(shape))


        except Exception as e:
            print(e)

main()