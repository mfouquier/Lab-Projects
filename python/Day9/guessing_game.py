import random

secret_number = random.randint(1, 100)

def check_number(num, secret): 
    if num == secret:
        return 0
    elif num > secret:
        return 1
    else:
        return -1
  
def set_difficulty(diff):
    if diff == 'easy':
        return 10
    else:
        return 5

def play_again():
    s_num = random.randint(1, 100)
    play_again = input("Would you like to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        guessing_game(s_num)
    else:
        pass

def guessing_game(secret_num):
    still_guessing = True
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    num_guesses = set_difficulty(difficulty)

    while still_guessing:
        print(f"You have {num_guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        status = check_number(guess, secret_num)
        if status == 0:
            print(f"I am 0, {status}")
            still_guessing = False
            print(f"You guessed it!!! The number was {secret_number}")
            play_again()
        elif status == 1:
            print(f"I am 1, {status}")
            num_guesses -= 1
            print("Too high.\nGuess again") 
        else:
            num_guesses -= 1
            print("Too low.\nGuess again.")


guessing_game(secret_number)
