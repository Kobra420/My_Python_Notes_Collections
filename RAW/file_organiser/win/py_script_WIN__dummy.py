import os
import shutil

def get_file_size(file_path):
    """
    Return the size of a file, given its file_path.

    :param file_path: a string representing the path of the file
    :return: an integer representing the size of the file in bytes
    
    return os.path.getsize(file_path)
    Return the size of a file, given its file_path.

    :param file_path: a string representing the path of the file
    :return: an integer representing the size of the file in bytes
    """
    return os.path.getsize(file_path)

def convert_bytes_to_megabytes(bytes_size):
    """
    Convert bytes to megabytes.

    :param bytes_size: an integer representing the size in bytes
        Args:
        bytes_size (int): The size in bytes to be converted.

    Returns:
        float: The size converted to megabytes.
    :return: a float representing the size in megabytes
    """
    return bytes_size / (1024 ** 2)

def organize_files_by_size(DIRECTORY_PATH, OUTPUT_FILE_PATH ):
    """
    Organize files by size and create sub-folders based on file size ranges.
    
    Args:
    - DIRECTORY_PATH: The path of the directory containing the files to be organized.
    - OUTPUT_FILE_PATH : The path of the output file where the organization details will be written.
    
    Returns:
    None
    
    This function takes in a directory path and an output file path. It then walks through the directory and collects file information (path and size) and sorts the files by size. It then creates sub-folders based on file size ranges and moves the files to the appropriate sub-folder. Finally, it writes the organization details to the output file.
    
    Example usage:
    organize_files_by_size('/your/directory/path', '/desired/output/file/path/output.txt')
    
    This will organize the files in the '/your/directory/path' directory by size and create sub-folders based on file size ranges. The organization details will be written to the '/desired/output/file/path/output.txt' file.
    """
    files = []
    
    # Collect file information (path and size)
    for dirpath, _, filenames in os.walk(DIRECTORY_PATH):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = get_file_size(file_path)
            files.append((file_path, size))

    # Sort files by size
    files.sort(key=lambda x: x[1])

    # Create sub-folders based on file size ranges
    # size_ranges = [(0, 1024), (1024, 10240), (10240, 102400), (102400, float('inf'))]
    size_ranges = [(1024000, 10240000), (10240000, float('inf'))]

    with open(OUTPUT_FILE_PATH , 'w', encoding='utf-8') as output_file:
        for file_path, size,filename in files:
            # Convert size to megabytes
            size_mb = round(convert_bytes_to_megabytes(size), 2)
            # output_file.write(f"File: {os.path.basename(file_path)}, Size: {size_mb} MB\n")
            output_file.write(f"File: {filename}, Size: {size_mb} MB\n")

            for size_range in size_ranges:
                if size_range[0] <= size < size_range[1]:
                    subfolder_path = os.path.join(DIRECTORY_PATH, f"Size_{size_range[0]}_{size_range[1]}")
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)

                    # Move the file to the appropriate subfolder
                    shutil.move(file_path, os.path.join(subfolder_path, os.path.basename(file_path)))
                    break

# Replace '/your/directory/path' with the actual path of your directory
DIRECTORY_PATH = r'E:\YT2024\BHARAT'
# Replace '/desired/output/file/path/output.txt' with your desired output file path
OUTPUT_FILE_PATH  = r'E:\YT2024\output_YT2024_Bharat.txt'

organize_files_by_size(DIRECTORY_PATH, OUTPUT_FILE_PATH )
