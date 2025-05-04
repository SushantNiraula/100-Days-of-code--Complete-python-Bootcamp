import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return EASY_LEVEL_TURNS if difficulty == 'easy' else HARD_LEVEL_TURNS

def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guessed_correctly = False
    while turns > 0 and not guessed_correctly:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        guessed_correctly = check_guess(guess, answer)
        if not guessed_correctly:
            turns -= 1

    if not guessed_correctly:
        print(f"You're out of guesses. You lose. The number was {answer}.")

if __name__ == "__main__":
    game()
