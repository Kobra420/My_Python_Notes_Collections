# computer random choice
# user chose difficulty easy or hard
# user guess
        # Easy 10 Hard 5
# user guess
# ----------
        # computer choice < user guess
                            # Too high.
                            # Guess again.
                            # You have 9 attempts remaining to guess the number.
        # computer choice > user guess
                            # Too low.
                            # Guess again.
                            # You have 9 attempts remaining to guess the number.
import random
import sys
import os
from art import logo
# welocome note
print(logo)
print("Welcome to the number guessing game.")
computer_choice = random.randrange(1,100)
turns = int()
user_difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
os.system('cls')
# computer random choice
def user_choice():
    """
    Generates the user's choice based on the user's selected difficulty.
    
    Returns:
        str: The user's difficulty choice.
    """
    global turns
    if user_difficulty_choice == "easy":
        turns = 10
        print("You have 10 attempts remaining to guess the number.")
    elif user_difficulty_choice == "hard":
        turns = 5
        print("You have 5 attempts remaining to guess the number.")
    else:
        print("Invalid input.")


# Step 2

def compare():
    """
    Compares the user's guess with the computer's choice 
    until the user guesses correctly or runs out of turns.
    Parameters:
        None
    Returns:
        None
    """
    global turns
    while turns >= 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_choice:
            print(f"You got it! The answer was {computer_choice}.")
            break
        elif user_guess > computer_choice:
            print("Too high.")
            turns -= 1
            if turns == 0:
                print()
                break
            print(f"You have {turns} attempts remaining to guess the number.")
        elif user_guess < computer_choice:
            print("Too low.")
            turns -= 1
            if turns == 0:
                print()
                break
            print(f"You have {turns} attempts remaining to guess the number.")
    if turns == 0:
        print("You've run out of guesses, you lose.")


# Step 3
user_choice()

compare()
sys.exit