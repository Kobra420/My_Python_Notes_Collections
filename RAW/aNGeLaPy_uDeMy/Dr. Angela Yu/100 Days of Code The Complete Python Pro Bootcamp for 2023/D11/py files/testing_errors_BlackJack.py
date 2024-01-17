# imports
from art_blackjack import logo
import random
import os
import sys
# Importing os and time module
import time

welcome = """
    Welcome to Blackjack!
    The dealer will draw two cards for you and one card for the dealer.
    You will then be asked to draw another card or not.
    If you draw another card, you will be given the sum of the two cards.
    If you do not draw another card, you will be given the sum of the two cards.
    If you draw a card that is a '1', you will be given a '11'.
    If you draw a card that is a '10', you will be given a '10'.
    If you draw a card that is a 'J', 'Q', or 'K', you will be given a '10'.
    If you draw a card that is a 'A', you will be given a '1' or '11'.
    If you draw a card that is a '2', '3', '4', '5', '6', '7', '8', '9', '10', you will be given the number.
    """
# # declarations

# # card
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# # dealing hands terms variable for Pc and User
deal = 0

# # count of user's card drawn
count = 0
# cleaning the screen
def clean():
    """We define our own clean function to clear the screen"""
    # TODO have to ask ai
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For macOS and Linux
    else:
        _ = os.system('clear')


def start_game():
    while True:
        user_choice_of_game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_choice_of_game_start == 'y':
            return True
        elif user_choice_of_game_start == 'n':
            print("Starting the game again")
            continue

        elif user_choice_of_game_start != 'y' and user_choice_of_game_start != 'n':
            print("Wrong input. Please run the game again.")
            time.sleep(10)
            return False


def continue_dealing():
    global deal, cards, count
    if deal == 0:
        user_get_more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_get_more_cards == 'y':
            count += 1
            return True
        elif user_get_more_cards == 'n':

            return False
    elif deal == 1:
        return "Now PC is dealing cards for itself"
        # pc_get_more_cards = random.choice(cards)
        # return pc_get_more_cards


# dealing the cards from random
def first_dealing():
    global cards
    first_hand = random.sample(cards, 2)
    return first_hand


def dealing_afterwards(lst0):
    previous_hand = lst0
    new_card_add = random.choice(cards)
    previous_hand.append(new_card_add)
    modified_hand = previous_hand
    if 11 in modified_hand and len(modified_hand) > 2:
        modified_hand.remove(11)
        modified_hand.append(1)
    return modified_hand


def add_cards(lst0):
    total = 0
    for k in lst0:
        total = total + k
    return total


def calculation(user,pc):
    user_score = add_cards(user)
    pc_score = add_cards(pc)
    if user_score == 21 and len(user) == 2:
        print("Win with a Blackjack 😎")
    elif pc_score == 21 and len(pc) ==2:
        print("Lose, opponent has Blackjack 😱")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif pc_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score < 21 and pc_score < 21:
        if user_score > pc_score:
            print("You win 😃")
        elif user_score == pc_score:
            print("Draw 🙃\n")
        else:
            print("You lose 😤")


def game():
    global deal, count
    while start_game():
        user_card = first_dealing()
        pc_card = first_dealing()
        user_score = add_cards(user_card)
        pc_score = add_cards(pc_card)
        print(f"User's First Hand:{user_card}\tUser's first Score:{user_score}\n", end='')
        print(f"First card of PC's Hand:{pc_card[0]}\tPC Score:{pc_score}")
        if not continue_dealing():
            print(f"PC's Final Hand{pc_card}\tPC's Final Score{pc_score}")
            calculation(user_card, pc_card)
            break
            sys.exit()
        else: # while continue_dealing():
            dealing_afterwards(user_card)
            user_score = add_cards(user_card)
            print(f"User's current hand:{user_card}\tUser's current score:{user_score}\n", end='')
        deal = 1
        continue_dealing()
        time.sleep(10)
        while count != 0:
            dealing_afterwards(pc_card)
            count -= 1
        pc_score = add_cards(pc_card)
        print(f"PC's Final Hand{pc_card}\tPC's Final Score{pc_score}")
        

# Clearing the Screen after 10-second halt '''

print(logo)
time.sleep(10)
clean()
print(welcome)
time.sleep(10)
clean()
game()
