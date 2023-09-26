# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
mapi = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#      V   1    2   3
#row1 = ["00","01","02"]     H 1
#row2 = ["10","11","12"]       2
#row3 = ["20","21","22"]       3
# Write your code below this row 👇

if position[0] == "1" and position[1] == "1":
    mapi[0][0] = "X"
if position[0] == "2" and position[1] == "1":
    mapi[0][1] = "X"
if position[0] == "3" and position[1] == "1":
    mapi[0][2] = "X"
if position[0] == "1" and position[1] == "2":
    mapi[1][0] = "X"
if position[0] == "2" and position[1] == "2":
    mapi[1][1] = "X"
if position[0] == "3" and position[1] == "2":
    mapi[1][2] = "X"
if position[0] == "1" and position[1] == "3":
    mapi[2][0] = "X"
if position[0] == "2" and position[1] == "3":
    mapi[2][1] = "X"
if position[0] == "3" and position[1] == "3":
    mapi[2][2] = "X"

# print(mapi)

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# 🚨🚨👇👇👇👇👇Dr. YU's CODE👇👇👇👇👇👇👇👇🚨🚨


# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# < STEP BY STEP>
# ---###       selected_row = map [vertical - 1]
# ---###       selected_row[horizontal - 1] = "X"

# < SHORTCUT >
# map[vertical - 1][horizontal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")
