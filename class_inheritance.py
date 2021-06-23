class Shape():
    def __init__(self, l, w):
        self.length = l
        self.width = w
        print("{} created.".format(self.__class__.__name__))
    def get_perim(self):
        return (self.length * 2) + (self.width * 2)
    def get_area(self):
        return self.length * self.width
    def what_am_i(self):
        print("I am a {}.".format(self.__class__.__name__))

class Square(Shape):
    pass

class Rectangle(Shape):
    pass

s1 = Square(3, 3)
r1 = Rectangle(8, 4)

s1.what_am_i()
r1.what_am_i()


