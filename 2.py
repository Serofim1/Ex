import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius**2) * math.pi
circle = Circle(5)
print (circle.area())
