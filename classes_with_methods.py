# Create rectangle and square classes with a method called calculate_perimeter that calculates the perimeter of the shapes they represent. Create Rectangle and Square objects and call the method on both of them.

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
        print("Rectangle created.")
    def calculate_perimeter(self):
        x = (self.length + self.width) * 2
        return x
        
class Square():
    def __init__(self, l):
        self.length = l
        print("Square created.")
    def calculate_perimeter(self):
        x = self.length * 4
        return x
        
r1 = Rectangle(4,5)
s1 = Square(12)
r1.calculate_perimeter()
s1.calculate_perimeter()