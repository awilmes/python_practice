class Student:
    def __init__(self, a, l, m, g):
        self.age = a
        self.level = l
        self.major = m
        self.gpa = g
        print("Created new student.")

    def summary(self):
        attributes = print(self.age,"\n",
                      self.level,"\n",
                      self.major,"\n",
                      self.gpa)
        return attributes

s1 = Student(18, "Senior", "Electrical Engineering", 4.0)
#Don't put a print statement here or Python will print "None"
s1.summary()
