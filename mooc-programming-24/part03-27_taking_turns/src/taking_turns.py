# Write your solution here
number = int(input("Please type in a number: "))
i = 0

if number % 2 == 0:
    while i != number:
        i += 1
        print(i)
        print(number)
        number -= 1
else:
    while i < number:
        i += 1 #1 #2 #3
        print(i)
        if i != number:  
            print(number) 
        number -= 1 #4 #3
    