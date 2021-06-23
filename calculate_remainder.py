# Calculate a remainder (given a numerator and denominator)

numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))
equation = "\nProblem to be solved: {} / {}".format(numerator, denominator)

print(equation)

def calculateRemainder(numerator, denominator):
    remainder = numerator % denominator
    return "The remainder is {}.".format(remainder)

calculateRemainder(numerator, denominator)