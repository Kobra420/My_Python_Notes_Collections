import random

def roll_dice():
    """
    Simulate a six-sided dice roll.
    """
    return random.randrange(1, 7)

# Simulate rolling the dice 5 times
for _ in range(5):
    result = roll_dice()
    print("Dice Roll Result:", result)
