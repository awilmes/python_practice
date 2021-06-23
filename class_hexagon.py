class Hexagon():
    def __init__(self, l):
        self.length = l
        print("Created!")

    def calculate_perimeter(self):
        perimeter = self.length * 6
        return perimeter
