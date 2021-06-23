#Print all the numbers form 25 to 30.

#for i in range(25,31):
#    print(i)

#Print each item in the list and their indexes.

#tv = ["The Walking Dead", "Entourage", "The Sopranos", "The vampire Diaries"]
#
#index = 1
#for i in tv:
#    strindex = str(index)
#    print(strindex + ". " + i)
#    index += 1

#Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a
# number on the list and tell them whether or not they guessed correctly.

#while True:
#    ns = ["1", "3", "5", "7", "9"]
#    a = input("Guess a number between 1-10: ")
#    if a == "q":
#        break
#    if a in ns:
#        print("You guessed correctly!")
#        break
#    if a not in ns:
#        print("Guess again.")

#tv = ["GOT", "Narcos", "Vice"]
#i = 0
#for show in tv:
#    new = tv[i]
#    new = new.upper()
#    tv[i] = new
#    i += 1
#
#print(tv)

#people = ["G. Bluth II",
#          "Barney",
#          "Dennis",
#          "Cartman",
#          "Stan",
#          "Kenny"]
#
#i = range(2,4)
#
#for i in people:
#    print(i)

#tv = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
#
#index = 1
#for i in tv:
#    str_index = str(index)
#    print(str_index + ". " + i)
#    index += 1

#qs = ["What is your name?",
#      "What is your fav. color?",
#      "What is your quest?"]
#n = 0
#while True:
#    print("Type q to quit")
#    a = input(qs[n])
#    if a == "q":
#        break
#    n = (n + 1) % 3


# Multiply all the numbers in the list with all the numbers in the other list.
# Append each result to a third list.

n1 = [8, 19, 148, 4]
n2 = [9, 1, 33, 83]
n3 = []

n = 0
for i in n1:
    result = n1[n] * n2[n]
    n3.append(result)
    n += 1

print(n3)











    
    
