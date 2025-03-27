from dataclasses import dataclass
from math import sqrt

numeric = int | float

@dataclass(eq=True, order=True)
class Punto:
    x: numeric
    y: numeric

    def distancia(self, other: "Punto") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Punto(3, 2)
p2 = Punto(1, 4)
print(p1.distancia(p2)) 
