import pandas as pd

# Read the NATO phonetic alphabet CSV
df = pd.read_csv('../26. Day26-List Comprehension/nato_phonetic_alphabet.csv')

# Create the NATO phonetic dictionary
nato_dict = {row.letter: row.code for index, row in df.iterrows()}

def generate_phonetic():
    while True:
        user_input = input("Enter a word: ").upper()
        try:
            # Create the phonetic list
            phonetic_list = [nato_dict[i] for i in user_input]
            return phonetic_list
        except KeyError:
            print("Sorry, only letters in the alphabet please.")

# Print the result
print(generate_phonetic())


