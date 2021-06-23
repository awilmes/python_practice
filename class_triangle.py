class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Created!")

    def area(self):
        area = 0.5 * self.base * self.height
        return area

t1 = Triangle(4, 3)
print(t1.area())
