#Write a while-loop and inside of your while-loop count down backward form 10 to 0.

while True:
    i = 10
    while i >= 0:
        print(i)
        i -= 1
    if i < 0:
        break
