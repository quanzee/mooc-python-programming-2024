# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")
character_index = word.find(character)

if len(word) - character_index >= 3:
    substring = word[character_index:character_index + 3]
    print(substring)

