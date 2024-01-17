# assignment 8
# Write a program that works out whether if a given number is an odd or even number.
#
# Even numbers can be divided by 2 with no remainder.
#
# e.g. 86 is even because 86 ÷ 2 = 43
#
# 43 does not have any decimal places. Therefore, the division is clean.
#
# e.g. 59 is odd because 59 ÷ 2 = 29.5
#
# 29.5 is not a whole number, it has decimal places. Therefore, there is a remainder of 0.5, so the division is not
# clean.
#
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g.
# 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# therefore: 14 % 4 = 2
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# n=int(number)
# z=n%2
# if z==0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# assignment 9
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should round the result to the nearest whole number.
# The interpretation message needs to include the words in bold from the interpretations above.
# e.g. underweight, normal weight, overweight, obese, clinically obese.

# Example Input
# weight = 85
# height = 1.75
# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325
# Your BMI is 28, you are slightly overweight.
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# bmi1 = (weight // (height ** 2))
# print(f"Actual bmi:{bmi1}")
# bmi = round(bmi1)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")
