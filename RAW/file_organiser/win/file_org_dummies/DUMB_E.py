# path Manipulation
from importlib.metadata import files
import os

# Join path components
full_path = os.path.join("C:\\", "Users", "User", "Documents", "Doc1.docx")
print("Full Path:", full_path)
# Get the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Change the current working directory to a different path
new_directory = r"P:\PROJECT_python\GIT\File_organizations"  # Remove "example1.txt" from the path
os.chdir(new_directory)

# Get the updated current working directory
updated_directory = os.getcwd()
print("Updated Working Directory:", updated_directory)
files = []
# Collect file information (path and size)
for dirpath, _, filenames in os.walk(DIRECTORY_PATH):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        size = get_file_size(file_path)
        files.append((file_path, size))