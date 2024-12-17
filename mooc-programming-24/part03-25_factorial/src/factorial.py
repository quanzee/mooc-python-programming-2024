# Write your solution here

number = int(input("Please type in a number: "))
i = 1
factorial = 1

while number > 0:
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")
    number = int(input("Please type in a number: "))
    i = 1
    factorial = 1
    

print("Thanks and bye!")

