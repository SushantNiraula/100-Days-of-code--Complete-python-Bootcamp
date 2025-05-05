#TODO: Create a letter using starting_letter.txt

def open_letter():
    with open('./Input/Letters/starting_letter.txt', 'r') as file:
        letter = file.read()
        print(letter)
        file.close()
        return letter

def open_names():
    with open ('./Input/Names/invited_names.txt', 'r') as file:
        names = file.readlines()
        print(names)
        file.close()
        return names

letter=open_letter()
names=open_names()
formatted_names=[]
for name in names:
    name=name.strip()
    formatted_names.append(name)
print(formatted_names)
for name in formatted_names:
    temp_letter=letter.replace('[name]',name)
    with open(f'./Output/ReadyToSend/{name}.txt', 'w') as file:
        file.write(temp_letter)
        file.close()



#for each name in invited_names.txt

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp