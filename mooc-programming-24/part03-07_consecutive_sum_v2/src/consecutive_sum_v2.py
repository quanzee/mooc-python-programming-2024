# Write your solution here
limit = int(input("Limit: "))
number = 1
sum = 1
sentence = "The consecutive sum: 1"

while sum < limit:
    number += 1
    sum += number
    sentence += f" + {number}"

sentence += f" = {sum}"
print(sentence)