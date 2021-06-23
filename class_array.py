class Square():
    sqs = []
    
    def __init__(self, l):
        self.length = l
        self.sqs.append(self.length)
        print("{} created.".format(__class__.__name__))
        
s1 = Square(2)
s2 = Square(4)
s3 = Square(9)

print(Square.sqs)