# Reverse a sentence ("bob likes dogs" -> "dogs likes bob")

sentence = "sentence to be reversed"
words = sentence.split(" ")

index = -1
for i in words:
    print(words[index], end = " ")
    index -= 1