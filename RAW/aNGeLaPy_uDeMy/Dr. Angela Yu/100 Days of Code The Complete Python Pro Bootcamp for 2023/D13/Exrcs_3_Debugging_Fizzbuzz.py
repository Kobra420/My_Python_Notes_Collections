for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:   # or vs and problem
        print("FizzBuzz")
        continue # cnotinue code wasn't there
    if number % 3 == 0:
        print("Fizz")
        continue  # cnotinue code wasn't there
    if number % 5 == 0:
        print("Buzz")
        continue  # cnotinue code wasn't there
    else:
        print(number)  # [] problem