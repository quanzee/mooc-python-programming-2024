# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
substring_index = string.find(substring)
second_string = string[substring_index + len(substring) + 1:]
first_substring = len(string) - len(second_string)

if substring in second_string:
    second_substring_index = (second_string.find(substring)+ first_substring)
    print(f"The second occurrence of the substring is at index {second_substring_index}.")
else:
    print("The substring does not occur twice in the string.")




