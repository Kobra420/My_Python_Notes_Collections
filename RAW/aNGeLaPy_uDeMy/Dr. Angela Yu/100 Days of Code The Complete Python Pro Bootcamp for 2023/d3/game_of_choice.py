import game_of_choice_art
import time

print("\n\n\nWelcome to Treasure Island.\n\n\n")
print(game_of_choice_art.welcome)
print("\n\n\nYour mission is to find the treasure.\n\n\n")
time.sleep(10)
print('You\'re at the cross road, where do you want to go? Type "Left" or "Right". \n\n')
print(game_of_choice_art.cross_road)
time.sleep(3)
selection1 = input("Enter Choice").lower()

if selection1 == "left":
    print(f'''You\'ve come to a River of Honey.\n There is an island in the middle of the lake. 
          \nType "wait" to wait for a boat.\n{game_of_choice_art.wait}\n Type "swim" to swim across.\n{game_of_choice_art.swim}\n''')
    selection2 = input().lower()
    if selection2 == "wait":
        print(game_of_choice_art.wait)
        time.sleep(5)
        print(game_of_choice_art.boat)
        time.sleep(6)
        print(f'\n\nYou arrive at the island unharmed.\n\n There is a house with 3 gates.\n\tOne red, one yellow and one blue. \nWhich colour do you choose?')
        print(f"{game_of_choice_art.red}\n{game_of_choice_art.Or}\n{game_of_choice_art.yellow}")
        print(f"\n{game_of_choice_art.Or}\n{game_of_choice_art.blue}")
        selection3 = input().lower()
        if selection3 == "yellow":
            time.sleep(5)
            print('You found the treasure! You Win!')
        elif selection3 == "red":
            print(f'You\'re being burned by fire..\n {game_of_choice_art.hell}{time.sleep(3)}\nGame Over.\n\n {time.sleep(3)}{game_of_choice_art.dead}')
        elif selection3 == "blue":
            print(f'Wrong Turn !! You\'ve become a prey to the beasts!!\n\t\n{game_of_choice_art.beast}{time.sleep(5)}\n Game Over.\n\n {time.sleep(3)}{game_of_choice_art.dead}')
        else:
            print('mentioned colour doesn\'t exists.\n  Game Over.\n\n {time.sleep(3)}{game_of_choice_art.dead}')            
    else:
        print(game_of_choice_art.swim)
        time.sleep(5)
        print(f'You\'ve got attacked by an angry Shark. Game Over.\n\n {time.sleep(3)}{game_of_choice_art.dead}')