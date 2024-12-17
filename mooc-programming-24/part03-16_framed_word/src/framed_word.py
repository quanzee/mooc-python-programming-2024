# Write your solution here
word = input("Word: ")
remainder_one_side = int((30 - len(word))/2 - 1)

print("*"*30)
if len(word) % 2 == 0:
    print("*" + " "*remainder_one_side + word + " "*remainder_one_side + "*")
else:
    print("*" + " "*remainder_one_side + word + " "*(remainder_one_side+1) + "*")
print("*"*30)
