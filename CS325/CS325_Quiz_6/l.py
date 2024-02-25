from abc import ABC, abstractclassmethod
class Shapes(ABC):
    @abstractclassmethod
    def getArea(self):pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14159265 * self.radius *self.radius

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side *self.side

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width *self.height
    
## add the triadnle class and def
class Triangle(Shapes):
    def __init__ (self, base, length):
        self.base = base
        self.length = length

    def getArea(self):
        return self.base * self.length * .5


def main():
    #test output
    shapes = [Circle(111), Square(222), Rectangle(333, 444) , Triangle(555,666)]

    for shape in shapes:
        print(shape.getArea())

if __name__ == "__main__":
    main()