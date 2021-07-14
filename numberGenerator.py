import random

fileName = "moreNumbers.txt"

with open(fileName, 'w') as out:
    for i in range(100):
        n = str(random.randint(0, 100)) + ", "
        print(n)
        out.write(n)