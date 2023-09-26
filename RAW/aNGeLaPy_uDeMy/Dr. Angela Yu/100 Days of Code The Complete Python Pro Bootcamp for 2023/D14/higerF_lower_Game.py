import random
import art
from game_data import data


def data_format(account):    
    """Format account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


selection_a = random.choice(data)

selection_b = random.choice(data)

if selection_a == selection_b:
    selection_b = random.choice(data)

print(art.logo1)
print(f"A\n{data_format(selection_a)}")
print(art.logo2)
print(f"B\n{data_format(selection_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

if selection_a["follower_count"] > selection_b["follower_count"]:
    answer = "A"
elif selection_a["follower_count"] < selection_b["follwer_count"]:
	answer = "B"
else:
    answer = "A"

print(answer)

if guess == answer:
    print("You are right!")
else:
    print("You are wrong!")




# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.