import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words=['Nepali','Country','Beautiful','Python','Programming','Language','Computer','Science']
for i in range(len(words)):
    words[i]=words[i].lower()
print('Welcome to Hangman')
## 1. Choose a random word from the list
word=random.choice(words)
print(word)
## 4. create a place holder with same no of blanks as letters in the word.
for i in range(len(word)):
    print('_',end='')
print()

## 2. Ask the user to guess a letter and assign their input to a variable
## 6. Use a while loop to let the user guess until they get it right
game_over=False
guessed_word=[]
wrong_guesses=0 
print(len(stages))
while not game_over:
    guess=input('Guess a letter: ').lower()
    if guess in guessed_word:
        print('You have already guessed that letter')
        continue

## 3. Check if the letter is in the word
## 5. Create a display that puts the guessed letter in the correct position
#7. change the for loop so that you keep the previous letters guessed
    display=''
    for letter in word:
        if letter==guess:
            display+=letter
            guessed_word.append(letter)
        elif letter in guessed_word:
            display+=letter
        else:
            display+='_'
    print(display)
    if guess not in word:
        
        wrong_guesses+=1
        print(stages[wrong_guesses])
    else:
        print('')
        print(stages[wrong_guesses])    
    
    if wrong_guesses==6:
        print('You lose')
        game_over=True

    if '_' not in display:
        print('You win')
        game_over=True
print()
