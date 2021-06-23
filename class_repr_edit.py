# Create a Square class that has one method that calculates its perimeter
# When you print a Square object, a message should print telling you the length of each of the four sides of the shape. For example, the code print(Square(29)) should print "29 by 29 by 29 by 29".

class Square():
    def __init__(self, l):
        self.length = l
        
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)
        
    def calc_perim():
        return self.length * 4
    
print(Square(29))