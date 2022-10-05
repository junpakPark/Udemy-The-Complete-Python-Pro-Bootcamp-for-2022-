with open("Input/Names/invited_names.txt") as file:
    arr = list(file.read().split('\n'))

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

for i in arr:
    with open(f"Output/ReadyToSend/Dear_{i}.txt", mode="w") as file:
        contents = letter[0].replace("[name]", i) + ''.join(i for i in letter[1:])
        file.write(contents)

with open("Input/Names/invited_names.txt") as file:
    arr = list(file.read().split('\n'))

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

for i in arr:
    with open(f"Output/ReadyToSend/Dear_{i}.txt", mode="w") as file:
        contents = letter[0].replace("[name]", i) + ''.join(i for i in letter[1:])
        file.write(contents)

# Angela code
# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
