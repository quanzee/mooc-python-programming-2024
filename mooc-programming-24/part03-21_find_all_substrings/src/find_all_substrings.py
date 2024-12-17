# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")
character_index = word.find(character)


while character_index != -1 and len(word) - character_index >= 3:
    substring = word[character_index:character_index + 3]
    print(substring)
    word = word[character_index + 1:]
    character_index = word.find(character)