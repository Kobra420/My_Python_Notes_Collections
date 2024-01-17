# Type error wrong datatype
year = int(input("Which year do you want to check?")) # int() converts string to integer wasn't applied before

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")