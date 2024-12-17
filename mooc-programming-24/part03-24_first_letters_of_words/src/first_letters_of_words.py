# Write your solution here
sentence = input("Please type in a sentence: ")

print(sentence[0])
i = 0

while i < len(sentence)-1: #r t #3total #last index is 2
    i += 1 #1 
    if sentence[i] == " ":
        print(sentence[i+1]) #2
    
