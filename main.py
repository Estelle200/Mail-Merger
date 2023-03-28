#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    


with open("./Input/Names/invited_names.txt", "rt") as names:
    for name in names:
        new_name = name.strip("\n")
        with open("Input/Letters/starting_letter.txt", "r") as letter:
            content = letter.read()
            content = content.replace("[Name]", new_name)

        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as send:
            send.write(content)

        


