import pandas as pd
df=pd.read_csv('nato_phonetic_alphabet.csv')


#{ "A":"Alpha","B":"Bravo"}
nato_dict={row.letter:row.code for index, row in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input=input("Enter a word: ").upper()

phonetic_list=[nato_dict[i] for i in user_input ]
print(phonetic_list)