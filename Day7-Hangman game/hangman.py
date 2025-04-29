import random
words=['Nepali','Country','Beautiful','Python','Programming','Language','Computer','Science']
for i in range(len(words)):
    words[i]=words[i].lower()
print('Welcome to Hangman')
gap=""
game_word=random.choice(words)
print(game_word)

for i in range(len(game_word)):
    print("_",end='')
print()
guess=input('Guess a character : ' ).lower()
display=''
while display!=game_word:
    for letter in game_word:
        if letter== guess:
            display+=guess
        else:
            display+="_"
print(display)