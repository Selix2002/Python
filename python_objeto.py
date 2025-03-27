from math import sqrt
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __str__(self):
        return f"({self.x}, {self.y})"
 
    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)
 
    def __eq__(self, otro_punto):
        return (self.x == otro_punto.x) and (self.y == otro_punto.y)

    def GetX(self): 
        return self.x

    def GetY(self):  
        return self.y




punto_ini = Punto(3, 5)
punto_fin = Punto(3, 5)

distancia = sqrt((punto_ini.GetX() - punto_fin.GetX())**2 + (punto_ini.GetY() - punto_fin.GetY())**2)

print(f"La distancia entre los puntos es: {distancia}")
