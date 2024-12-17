# Write your solution here

number = int(input("Please type in a number: "))

x = 1
y = 1

while x <= number:
    print(f"{x} x {y} = {x*y}")
    y += 1
    if y > number:
        y = 1
        x += 1