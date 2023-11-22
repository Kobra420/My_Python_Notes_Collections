programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again.",
                          "Class": "A blueprint for creating objects.",
                          "Object": "An instance of a class."}
#looping through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
for value in programming_dictionary.values():
    print(value)
for key, value in programming_dictionary.items():
    print(f"{key}:{value}")
print(programming_dictionary)