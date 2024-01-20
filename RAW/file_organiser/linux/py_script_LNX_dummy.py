# linux
import os

def organize_files(directory_path):
    # List all files in the source folder
    files = os.listdir(directory_path)
    print(files)


organize_files(r'/media/cyborg23/experiments')