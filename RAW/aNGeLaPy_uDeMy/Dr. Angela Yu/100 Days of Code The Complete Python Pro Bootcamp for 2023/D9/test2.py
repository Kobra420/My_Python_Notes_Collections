# Menu-Driven Dictionary Operations

def display_menu():
    print("\nMenu:")
    print("1. Display Dictionary")
    print("2. Add Key-Value Pair")
    print("3. Update Value for a Key")
    print("4. Delete Key-Value Pair")
    print("5. Exit")

def display_dictionary(dictionary):
    print("\nCurrent Dictionary:")
    for key, value in dictionary.items():
        print(f"keys {key}: --> value -  {value}")

def add_key_value(dictionary):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dictionary[key] = value
    print(f"Key-Value Pair ({key}: {value}) added successfully.")

def update_value(dictionary):
    key = input("Enter the key to update: ")
    if key in dictionary:
        new_value = input(f"Enter the new value for {key}: ")
        dictionary[key] = new_value
        print(f"Value for {key} updated successfully.")
    else:
        print(f"Key {key} not found in the dictionary.")

def delete_key_value(dictionary):
    key = input("Enter the key to delete: ")
    if key in dictionary:
        del dictionary[key]
        print(f"Key-Value Pair with key {key} deleted successfully.")
    else:
        print(f"Key {key} not found in the dictionary.")

# Main Program
user_dictionary = {}
# Real-life data samples in a dictionary
real_life_data = {
    101: 25,
    205: 45,
    307: 12,
    412: 30,
    523: 18,
    608: 50,
    719: 22,
    821: 36
}

# Feel free to replace the values with whatever makes sense for your data!
user_dictionary = real_life_data

# #experimental
# for keys in user_dictionary:
#     print(f"key:-{keys} --> value - {user_dictionary[keys]}")

while True:
    display_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_dictionary(user_dictionary)
    elif choice == '2':
        add_key_value(user_dictionary)
    elif choice == '3':
        update_value(user_dictionary)
    elif choice == '4':
        delete_key_value(user_dictionary)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
