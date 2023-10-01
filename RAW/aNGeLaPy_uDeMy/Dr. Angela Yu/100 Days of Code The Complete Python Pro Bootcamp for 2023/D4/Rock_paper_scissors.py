import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Write your code below this line 👇

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

pc = [rock, paper, scissors]
Players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(len(pc))
# print(random.randint(0, 2))
# pc1 = pc[random.randint(0, (len(pc) - 1))])
Computers_choice = random.randint(0, (len(pc) - 1))
if Players_choice == 0:
    print("\n", rock)
    print(f"Computer chose:\n{pc[Computers_choice]}")
    if Computers_choice == 0:
        print("You Draw :| ")
    elif Computers_choice == 1:
        print("You Lost.Game Over :( ")
    else:
        print("You Win :) ")
elif Players_choice == 1:
    print("\n", paper)
    print(f"Computer chose:\n{pc[Computers_choice]}")
    if Computers_choice == 1:
        print("You Draw :| ")
    elif Computers_choice == 2:
        print("You Lost.Game Over :( ")
    else:
        print("You Win :) ")
elif Players_choice == 2:
    print("\n", scissors)
    print(f"Computer chose:\n{pc[Computers_choice]}")
    if Computers_choice == 2:
        print("You Draw :| ")
    elif Computers_choice == 0:
        print("You Lost.Game Over :( ")
    else:
        print("You Win :) ")
else:
    print("Invalid Input!! Please Enter values as per instructions.")