import math

class Circle():
    def __init__(self, r):
        self.radius = r 
        print("Created!")

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
    
c1 = Circle(2)
print(c1.area())
