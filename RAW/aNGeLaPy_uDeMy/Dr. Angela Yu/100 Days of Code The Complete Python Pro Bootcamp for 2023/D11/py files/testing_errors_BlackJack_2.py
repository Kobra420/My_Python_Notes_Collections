import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_blackjack():
    while True:
        user_start_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if user_start_blackjack == "n":
            return False
        elif user_start_blackjack == "y":
            return True
        else:
            print("Invalid Input")
            continue


def user_choice():
    user_input = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False


def sum_of_cards(lst):
    return sum(lst)


def calculation(usr, pc):
    if pc == 21:
        print("You Lose😤")
    elif usr == 21:
        print("Opponent went over. You win 😁")
    elif pc < 21 and usr < 21:
        if pc > usr:
            print("You Lose😤")
        if pc < usr:
            print("Opponent went over. You win 😁")
    elif pc > 21:
        print("Opponent went over. You win 😁")
    elif usr > 21:
        print("You Lose😤")


def first_time_card_selection():
    return random.sample(cards, 2)


def second_time_card_selection(lst):
    lst.append(random.choice(cards))
    if 11 in lst and sum_of_cards(lst) > 21:
        lst.remove(11)
        lst.append(1)
    return lst


while start_blackjack():
    user_card = first_time_card_selection()
    computer_card = first_time_card_selection()
    sum_of_user_cards = sum_of_cards(user_card)
    sum_of_computer_cards = sum_of_cards(computer_card)
    print(f"Your cards: {user_card}, current score: {sum_of_user_cards}\nComputer's first card [{computer_card[0]}] ")

    # Prompt for user's choice
    while sum_of_user_cards < 21:
        if user_choice():
            second_time_card_selection(user_card)
            sum_of_user_cards = sum_of_cards(user_card)
            print(f"Your cards: {user_card}, current score: {sum_of_user_cards}\nComputer's first card [{computer_card[0]}] ")
        else:
            second_time_card_selection(computer_card)
            sum_of_computer_cards = sum_of_cards(computer_card)
            break
    calculation(sum_of_user_cards, sum_of_computer_cards)
    print(f"Your cards: {user_card} final score: {sum_of_user_cards}\nComputer's final hand: [{computer_card}] final score: {sum_of_computer_cards} ")
