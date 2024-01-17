# number = int(input("Check this number: "))

# if number >= 1:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print("It's not a prime number")
#         else:
#             print("It's a prime number")

# Example list
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']

# Find the index of 'orange' in the list
index_of_orange = fruits.index('orange')

print(f"The index of 'orange' is: {index_of_orange}")

for fruit_index in fruits:
    print(fruits.index(fruit_index),end=' ')