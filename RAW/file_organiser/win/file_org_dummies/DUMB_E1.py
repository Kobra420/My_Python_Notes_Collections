import sys

# Function to print to both console and file
def print_and_save(text):
    # Print to console
    print(text)
    
    # Save to file
    with open('output.txt', 'a') as file:
        file.write(text + '\n')

# Redirect stdout to a file
sys.stdout = open('output.txt', 'w')

# Example usage
print_and_save("Hello, World!")
print_and_save("This is a test message.")

# Remember to reset stdout to the original value if needed
sys.stdout.close()
sys.stdout = sys.__stdout__