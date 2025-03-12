class Triangle():
    def __init__(self, h, a):
        self.height = h
        self.side = a

    def area(self):
        return (self.height/2)*self.side

triangle = Triangle(5, 10)
print(triangle.area())
