# win 
# os.stat
import os
path = r"P:\GIT4BothOS_Lnx_win\GIT\File_organizations\old BREW.txt"
# Get the status of a file
file_status = os.stat(path)
print("File Status:", file_status)
