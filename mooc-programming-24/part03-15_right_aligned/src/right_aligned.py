# Write your solution here

string = input("Please type in a string: ")
sentence = ""

if len(string) < 20:
    remainder = 20 - len(string)
    sentence += "*"*remainder + string
print(sentence)
