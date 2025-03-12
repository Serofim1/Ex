class Hexagon():
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.side1 = a1
        self.side2 = a2
        self.side3 = a3
        self.side4 = a4
        self.side5 = a5
        self.side6 = a6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
