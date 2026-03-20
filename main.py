PLACEHOLDER = "[name]"

with open("./Input/Names/our_contacts.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
# print(letter)

for name in names:
    name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, name)
   