class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        print("Created!")
    def calculatePerimeter(self):
        return (self.length*2)+(self.width*2)
    def changeSize(self):
        x = int(input("Enter multiplier: "))
        self.length = self.length * x
        self.width = self.width * x
        return print("Size increased {}x.".format(x))
        
        
class Square:
    def __init__(self, l):
        self.length = l
        print("Created!")
    def calculatePerimeter(self):
        return self.length * 4
    def changeSize(self):
        x = int(input("Enter the new size: "))
        self.length = x
        return print("Length changed to {}.".format(x))
