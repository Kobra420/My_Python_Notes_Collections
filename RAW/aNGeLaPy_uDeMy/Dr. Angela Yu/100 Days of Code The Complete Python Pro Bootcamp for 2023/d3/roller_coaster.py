if int(input("WHat is your height?(in centimeter)  ")) > 120:
    print("You can ride the Disney Safari")
    Age = int(input("Please mention your Age: "))
    if Age < 12:
        bill = 10
    if Age < 18:
        bill = 15
    if Age > 18:
        bill = 25
    if input("Would you like to say cheese while riding?Y/N ") == "Y":
        bill += 10
        print(f"You have to pay ₹{bill} in total")
    else:
        print(f"You have to pay ₹{bill} in total")

else:
    print("We are sorry.Your height is not eligible for the roller-coaster")
