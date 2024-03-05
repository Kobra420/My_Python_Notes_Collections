import sys
import os

# Change the current working directory to a different path
new_directory = r"P:\PROJECT_python\GIT\File_organizations"  # Remove "example1.txt" from the path
os.chdir(new_directory)

# Function to print to both console and file
def print_and_save(text):
    # Print to console
    print(text)
    
    # Save to file
    with open('output.txt', 'a') as file:
        file.write(text + '\n')

# Redirect stdout to a file
sys.stdout = open('output.txt', 'w')

# os.scandir(
# path = r"E:\YT2024\BANGLA"
path1 = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EA Games\Command and ConquerTM Generals Zero Hour"
# Iterate over entries in a directory
for entry in os.scandir(path1):
    print_and_save(entry.name)

# # Example usage
# print_and_save("Hello, World!")
# print_and_save("This is a test message.")

# Remember to reset stdout to the original value if needed
sys.stdout.close()
sys.stdout = sys.__stdout__
