# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
true1 = lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e")
true2 = lower_name2.count("t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")
love1 = lower_name1.count("l") + lower_name1.count("o") + lower_name1.count("v") + lower_name1.count("e")
love2 = lower_name2.count("l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e")
true = true1 + true2
love = love1 + love2
love_score = 10*true + love
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


# Madam LU's Code
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
