# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        final_bill = bill + 2
    if add_pepperoni == "N":
        final_bill = bill + 0
    if extra_cheese == "Y":
        final_bill += 1
    if extra_cheese == "N":
        final_bill += 0
    print(f"Your final bill is: ${final_bill}.")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        final_bill = bill + 3
    if add_pepperoni == "N":
        final_bill = bill + 0
    if extra_cheese == "Y":
        final_bill += 1
    if extra_cheese == "N":
        final_bill += 0
    print(f"Your final bill is: ${final_bill}.")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        final_bill = bill + 3
    if add_pepperoni == "N":
        final_bill = bill + 0
    if extra_cheese == "Y":
        final_bill += 1
    if extra_cheese == "N":
        final_bill += 0
    print(f"Your final bill is: ${final_bill}.")
else:
    print("Please enter valid inputs as mentioned above.")

#Madam LU's Code
# ▼
# ▼
# ▼

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")


