PLACEHOLDER = "[name"

with open("./Input/Names/invited_names.txt") as file_read:
    read_file = file_read.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in read_file:
        strip_name = name.strip()
        new_content = letter_content.replace(PLACEHOLDER, strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}",mode="w") as final_content:
            final_content.write(new_content)

