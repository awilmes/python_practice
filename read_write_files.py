#Read a file on your computer

#import os
#os.path.join("Python",
#             "Challenges",
#             "read_me.txt")
#
#fx = open("read_me.txt", "r")
#with open("read_me.txt", "r") as f:
#    print(f.read())
#fx.close()

#Write a program that asks a user a question, and saves their answer to a file.

#fx = open("user_input.txt", "w")
#fx.write(input("What is your name?"))
#fx.close()

# Write the lists to a .csv

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    for i in movies:
        write.writerow(i)
