# combination of dictionary and functions 

# add
def add(n1,n2):
    """ add two numbers n1 and n2"""
    return n1+n2

#substracton

def subtract(n1,n2):
    """ subtract n2 from n1"""

def multiply(n1,n2):
    """ multiply n1 and n2"""
    return n1*n2

#division

def div(n1,n2):
    """ divide n1 by n2"""
    return n1/n2

operations ={}

operations['+'] = add

operations['-'] = subtract

operations['*'] = multiply

operations['/'] = div

num1=int(input("What's the first number? "))
num2=int(input("What's the second number? "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above ")

calculation_function = operations[operation_symbol]

answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

#dictionary is a collection of key value pairs
