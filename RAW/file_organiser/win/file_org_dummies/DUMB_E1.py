import sys
import os

# Change the current working directory to a different path
new_directory = r"P:\GIT4BothOS_Lnx_win\GIT"  # Remove "example1.txt" from the path
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

# Target folder to be scanned

# os.scandir(
# path = r"E:\YT2024\BANGLA"
path1 = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EA Games\Command and ConquerTM Generals Zero Hour"

# Iterate over entries in a directory
for entry in os.scandir(path1):
    print_and_save(entry.name)

def print_subfolders_in_folder(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                print(entry.name)

# Specify the path to the folder you want to scan
# folder_path = 'path_to_your_folder'
folder_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EA Games"

# Call the function to print subfolders in the specified folder
# print_subfolders_in_folder(folder_path)
# # Example usage
print_and_save(print_subfolders_in_folder(folder_path))
# # Example usage
# print_and_save("Hello, World!")
# print_and_save("This is a test message.")

# Remember to reset stdout to the original value if needed
sys.stdout.close()
sys.stdout = sys.__stdout__
