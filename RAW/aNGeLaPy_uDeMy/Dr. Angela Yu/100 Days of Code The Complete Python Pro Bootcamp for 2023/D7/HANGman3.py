list = ["aardvark", "baboon", "camel"]
import random
word = random.choice(list)
blanks = "_  " * len(word)
# blanks = "0123456789"
print("LOL " + word)
guess = input("Guess a letter: ")
for i in range(len(word)):
    if word[i] == guess:
        blanks = blanks[:i*3] + guess + blanks[i*3+1:]  #  i*3 for "_  " three strings in the blanks
# you can add i*2 for "_ "two strings and [:i] & [i+1]  for no spaces
print(blanks)