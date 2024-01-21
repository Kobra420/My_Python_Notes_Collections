# linux
import os
import subprocess

directory_path = r"/media/cyborg23/experiments_E/YT2024/BHARAT"
# output_file_path = r"/media/cyborg23/experiments_E/YT2024/Bharat_2024_list.txt"
output_file_path = r"/home/cyborg23/Videos/YT_2024_Bharat.txt"

def organize_files(directory_path):
    """_summary_
    Parameters:
        directory_path (_type_): _description_

    Returns:
        _type_: _description_
        
    Args:
        directory_path (_type_): _description_
    """
    # List all files in the source folder
    files = os.listdir(directory_path)
    # print(files)


def get_file_size(file_path):
    return os.path.getsize(file_path)

def print_file_sizes(directory_path, output_file_path):
    """
    # Use the touch command to create the output file
    subprocess.run(['touch', output_file_path])

    with open(output_file_path, 'w') as output_file:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                size = get_file_size(file_path)
                output_file.write(f"File: {file_path}, Size: {size} bytes\n")
    """
    #global
    # global directory_path, output_file_path
    # Use the touch command to create the output file
    subprocess.run(['touch', output_file_path], check=True)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                
                size = (get_file_size(file_path))/ 2048
                output_file.write(f"File: {filename}, Size: {size} MB\n\n")


# organize_files(directory_path)
print_file_sizes(directory_path, output_file_path)