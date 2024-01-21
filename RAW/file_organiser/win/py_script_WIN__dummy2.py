import os
import shutil

def get_file_size(file_path):
    return os.path.getsize(file_path)

def organize_files_by_size(directory_path, output_file_path):
    files = []
    
    # Collect file information (path and size)
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = get_file_size(file_path)
            files.append((file_path, size))

    # Sort files by size
    files.sort(key=lambda x: x[1])

    # Create subfolders based on file size ranges
    size_ranges = [(0, 1024), (1024, 10240), (10240, 102400), (102400, float('inf'))]

    for file_path, size in files:
        for size_range in size_ranges:
            if size_range[0] <= size < size_range[1]:
                subfolder_path = os.path.join(directory_path, f"Size_{size_range[0]}_{size_range[1]}")
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

                # Move the file to the appropriate subfolder
                shutil.move(file_path, os.path.join(subfolder_path, os.path.basename(file_path)))
                break

    # Print the file-size output to a text file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path, size in files:
            output_file.write(f"File: {file_path}, Size: {size} bytes\n")

# Replace '/your/directory/path' with the actual path of your directory
directory_path = r'E:\YT2024\BHARAT'

# Replace '/desired/output/file/path/output.txt' with your desired output file path
output_file_path = r'E:\YT2024\output.txt'

organize_files_by_size(directory_path, output_file_path)
