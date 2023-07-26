import math
from modelos.Conversions import Lineal,Surface

#Clase padre
class Figure:
    def AreaPerimeter(self):
        return self.Area(),self.Perimeter()
    
    def printCalcs(self, units="cm", precision=4):
        _area, _perimeter = self.AreaPerimeter()
        if units=="cm":
            _str = f"""
            This is a {self.name} 
            Area: {round(_area,precision)}(cm2)
            Perimeter: {round(_perimeter,precision)}(cm)"""
        if units=="m":
            _str = f"""
            This is a {self.name} 
            Area: {Surface.cm2m(_area, precision)}(m2)
            Perimeter: {Lineal.cm2m(_perimeter, precision)}(m)"""

        print(_str)

#Circulo con radio en cm
class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius
        self.name = "Circle"

    def Area(self):
        return math.pi*self.radius**2
    
    def Perimeter(self):
        return 2*math.pi*self.radius

#Rectangulo con dimensiones en cm
class Rectangle(Figure):
    def __init__(self,base, height):
        self.base = base
        self.height = height
        self.name = "Rectangle"

    def Area(self):
        return self.base*self.height
    
    def Perimeter(self):
        return 2*self.base + 2*self.height
    
#Cuadrado con dimensiones en cm
class Square(Rectangle):
    def __init__(self,edge):
        super().__init__(base=edge, height=edge)
        self.name = "Square"