# Write your solution here
number = int(input("Please type in a number: "))

i = 1

while i <= number:
    if i == number:
        print(number)
        break
    else:
        print(i+1)
        print(i)
        i += 2