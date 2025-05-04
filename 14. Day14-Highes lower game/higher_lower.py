
from game_data import data
from logo import logo, vs
import random


def game():
    second_index=random.randint(0,len(data)-1)
    i=0
    while True:
        print(logo)
        if i>0:
            print(f"You are right your current score is: {i} ")
        a=second_index
        b=random.randint(0,len(data)-1)
        print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
        print(vs)
        print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
        answer=input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer=='A':
            if data[a]['follower_count']<data[b]['follower_count']:
                print(logo)
                print(f"Sorry that's wrong answer current answer is: {data[b]['name']} and final score is: {i}")
                break
            else:
                second_index=b
        else:
            if data[a]['follower_count']>data[b]['follower_count']:
                print(logo)
                print(f"Sorry that's wrong answer current answer is: {data[a]['name']} and final score is: {i}")
                break
            else:
                second_index=b
        i+=1

game()


## """ArithmeticError

"""
correct_answer = 'A' if a_followers > b_followers else 'B'

        if answer == correct_answer:
            score += 1
            current_index = b if correct_answer == 'B' else a
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break


"""
