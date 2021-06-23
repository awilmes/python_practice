#Check if a user input is even or odd.
#Check if the number is a multiple of 4.

#while True:
#    try:
#        print("Press q to quit")
#        uin = input("Enter a number: ")
#        if uin == "q":
#            break
#        uin = int(uin)
#        if uin % 2 > 0 or uin == 1:
#            print("You entered an odd number.")
#            continue
#        if uin % 4 == 0:
#            print("You entered a multiple of 4.")
#        else:
#            print("You entered an even number.")
#    except ValueError:
#        print("You fool! Entry was not a valid integer!")

#Ask the user for two numbers. One to check(num) and one to divide by(check).
#If check divides evenly into num, tell the user.

while True:
    try:
        print("Press q to quit")
        num = input("Enter a number to check: ")
        if num == "q":
            break
        num = int(num)
        check = input("Enter a number to divide by: ")
        check = int(check)
        result = num % check
        if num % check == 0:
            print("Successful match.")
        else:
            print("No match found. Remainder: {}".format(result))
    except ValueError:
        print("You fool! Enter a number! Not {}...".format(num))
