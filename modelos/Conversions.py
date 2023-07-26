import math

#Conversion lineal
class Lineal:
    def cm2m(cm, precision=2): #estatico no lleva self
        return round(cm/100,precision)
    
class Surface:
    def cm2m(cm, precision=2): #estatico no lleva self
        return round(cm/10000,precision)