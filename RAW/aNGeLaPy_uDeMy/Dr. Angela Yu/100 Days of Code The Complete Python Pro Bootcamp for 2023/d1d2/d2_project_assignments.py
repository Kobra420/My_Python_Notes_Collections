
#assignment 5
# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# Example Input
# 39
# Example Output
# 3 + 9 = 12
# 12


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

x=int(two_digit_number)//10
y=int(two_digit_number)%10
s=x+y
print("The summation of the two digits of the number is:\n ",s)
####################################
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(second_digit+first_digit)
print = (int(second_digit)+int(first_digit))
####################################


#assignment 6
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#######################
# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26
########################
# f=15.22
# print(int(f))
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇
# b=float(height)
# a=float(weight)
# bmi=a/(b*b)
# print(int(bmi))
#sol in that video
# bmi = int(weight) / float(height) **2


#assignment 7

# Create a program using maths and f-Strings that tells us
# how many days, weeks, months we have left if we live until 90 years old.
#
# It will take
# your current age as the input and output a message with our time left in this format:
#
# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
#
# Warning your output should match the Example Output format exactly,
# even the positions of the commas and full stops.
#
# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

#f strings example
# val = 'Geeks'
# print(f"{val}for{val} is a portal for {val}.")
#
# name = 'Tushar'
# age = 23
# print(f"Hello, My name is {name} and I'm {age} years old.")

# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# a=int(age)
# age_left=90-a
# days=age_left*365
# weeks=age_left*52
# months=age_left*12
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")


