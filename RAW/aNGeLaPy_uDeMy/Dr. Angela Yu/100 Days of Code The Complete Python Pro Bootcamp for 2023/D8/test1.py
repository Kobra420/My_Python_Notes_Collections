number = int(input("Check this number: "))

if number >= 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("It's not a prime number")
        else:
            print("It's a prime number")


