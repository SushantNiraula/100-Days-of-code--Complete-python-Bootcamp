
rock='''
 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
'''
paper='''

           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   

'''

scissors='''

    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

'''

def display_choice(user_choice):
    if user_choice ==1:
        print(rock)
    elif user_choice ==2:
        print(paper)
    elif user_choice ==3:
        print(scissors)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        exit()


print("Welcome to Rock, Paper, Scissors!")
print("Choose your weapon:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
user_choice = int(input("Enter your choice (1-3): "))


import random
computer_choice = random.randint(1, 3)
print("User's choice:")
display_choice(user_choice)
print("Computer's choice:")
display_choice(computer_choice)

if user_choice == computer_choice:
    print("It's a Tie.")
elif (user_choice==1 and computer_choice==3) or \
     (user_choice==2 and computer_choice==1) or \
     (user_choice==3 and computer_choice==2):
    print("User wins.")
elif (computer_choice==1 and user_choice==3) or \
     (computer_choice==2 and user_choice==1) or \
     (computer_choice==3 and user_choice==2):
    print("Computer wins.")
else:
    print("Invalid choice. Please choose 1, 2, or 3.")
    exit()
# The game is over.

