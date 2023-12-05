
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        #print(new_letter)

        with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", mode="w") as data:
            data.write(new_letter)
