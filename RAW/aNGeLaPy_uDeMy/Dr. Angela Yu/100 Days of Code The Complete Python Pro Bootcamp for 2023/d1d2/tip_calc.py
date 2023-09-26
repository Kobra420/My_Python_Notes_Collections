print("Welcome to the Tip calculator at L-BAR\n")
total = float(input("Enter the total cost:\n"))
num_ppl = float(input("How many people ro split the bill?\n"))
tip = float(input("How many percentage tip would you like to give? 10 ,12, 50 or 25?"))
percent = tip/100
pay = round((total / num_ppl) + ((total / num_ppl) * percent), 2)
pay = "{:.2f}".format(total/num_ppl)
if tip == int(tip):
    print(f"\nThanks for enthusiasm\nEach person should pay: {pay}")
elif tip == 50:
    print(f"\nEach person should pay: {pay}")
elif tip == 25:
    print(f"\nEach person should pay: {pay}")
elif tip == 10:
    print(f"\nEach person should pay: {pay}")
elif tip == 12:
    print(f"\nEach person should pay: {pay}")
else:
    print(f"\nWow!! you tipped {tip}.\nWe appreciate your support\nbut\nwe only accept round figures")


    