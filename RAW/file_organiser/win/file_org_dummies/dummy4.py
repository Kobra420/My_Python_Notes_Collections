"""
This module provides functionality for organizing files in a specified directory.
"""
# import os
import os
# import shutil
import shutil

# source = input("Enter the source folder name: ")
path = input("Enter source folder path: ")
files = os.listdir(path)

for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
