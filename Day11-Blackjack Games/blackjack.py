## First of all we ask the user whether he wants to play or not
## Definining constants:
logo="""
from astroid.nodes.node_classes import Break
 _     _            _    _            _
| |   | |          | |  (_)          | |
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |
                      |___|"""

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
over=False
import random
player_cards=[]
computer_cards=[]
def generate_first_cards():
    temp=[]
    temp.append(random.choice(cards))
    temp.append(random.choice(cards))
    while sum(temp)>21:
        temp.pop()
        temp.append(random.choice(cards))
    return temp

def generate_new_card(temp):
    temp.append(random.choice(cards))



def play_blackjack():
    while True:
        print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
        print(f'computers first card : {computer_cards[0]}')
        new_card=input('Type "y" to get another card, type "n" to pass: ')
        if new_card=='y':
            generate_new_card(player_cards)
            if sum(player_cards)>21:
                print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                print('You Lose')

                break
        else:
            while sum(computer_cards)<17:
                generate_new_card(computer_cards)

            if sum(player_cards)<21 and sum(computer_cards)<21:
                if sum(computer_cards)>sum(player_cards):
                    print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                    print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                    print("You lose, Computer wins.")
                    break

                elif sum(computer_cards)<sum(player_cards):
                    print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                    print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                    print("You Won")
                    break
                else:
                    print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                    print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                    print("Tie")
                    break


            elif sum(player_cards)>21:
                print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                print("You lose")
                break

            elif sum(computer_cards)>21:
                print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                print("You won")
                break

            else:
                print(f'Your cards :{player_cards}, current score: {sum(player_cards)}')
                print(f'computers first card : {computer_cards}, computer score: {sum(computer_cards)}')
                print("Tie")
                break



start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start=="y":
    print(logo)
    print("Welcome to the Blackjack Game: \n")
    player_cards=generate_first_cards()
    computer_cards=generate_first_cards()
    play_blackjack()
else:
    print("Thank you for playing!")
