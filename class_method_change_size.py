# Define a method in your Square class called change_size that allows you to pass in a number that increases or decreases (if the number is negative) each side of a Square object by that number.

class Square():
    def __init__(self, l):
        self.length = l
        print("Square created.")
    def calculate_perimeter(self):
        return self.length * 4
    def change_size(self, new_size):
        self.length += new_size

s1 = Square(5)

