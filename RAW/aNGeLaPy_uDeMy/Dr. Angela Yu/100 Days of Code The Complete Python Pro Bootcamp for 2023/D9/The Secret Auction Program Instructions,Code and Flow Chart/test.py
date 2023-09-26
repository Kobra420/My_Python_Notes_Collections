# import os
# from Art import logo
# print(logo)
# x = input()
# if x == 'y':
#     os.system('cls')
# else:
#     print("xxx")



# from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
from Art import logo

print(logo)


def check(check_other_bidders):
    if check_other_bidders.lower() == 'yes':
        return True
    else:
        return False


def bid_record():
    bidding_record = {}  # Empty dictionary to store the bidders and their bids

    check_other_bidders = input("Type 'yes' if there are other bidders, or 'no' to finish: ")
    while check(check_other_bidders):
        bidder = input("What is your Name?: ")
        bid_amount = float(input("What is your bid?: $"))
        bidding_record[bidder] = bid_amount  # Add the bidder and their bid to the record
        check_other_bidders = input("Type 'yes' if there are other bidders, or 'no' to finish: ")
        os.system('clear')  # Clears the screen before taking the second bid

    # print("Bidding record:", bidding_record)

    highest_bidder = ''
    highest_bid = 0

    # Find the highest bidder and their bid in the record
    for bidder, bid in bidding_record.items():
        if bid > highest_bid:
            highest_bidder = bidder
            highest_bid = bid

    print("Highest bidder:", highest_bidder)
    print("Highest bid:", highest_bid)


bid_record()
