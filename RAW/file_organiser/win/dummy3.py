import os
import shutil
import pandas as pd

def get_file_size(file_path):
    return os.path.getsize(file_path)

def convert_bytes_to_megabytes(bytes_size):
    return bytes_size / (1024 ** 2)

def convert_bytes_to_gigabytes(bytes_size):
    return bytes_size / (1024 ** 3)

def create_subfolders(directory_path, size_ranges, target_folder):
    subfolder_paths = []
    for size_range in size_ranges:
        subfolder_path = os.path.join(target_folder, f"Size_{size_range[0]}MB_{size_range[1]}MB")
        subfolder_paths.append(subfolder_path)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
    return subfolder_paths

def organize_files_and_write_to_excel(directory_path, output_file_path, size_ranges, target_folder):
    files = []
    
    # Collect file information (path and size)
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = get_file_size(file_path)
            files.append((file_path, size))

    # Sort files by size
    files.sort(key=lambda x: x[1])

    # Create subfolders based on specified size ranges
    subfolder_paths = create_subfolders(directory_path, size_ranges, target_folder)

    # Write file names and sizes to Excel
    data = {'File Name': [], 'File Size (MB)': []}

    for file_path, size in files:
        size_mb = round(convert_bytes_to_megabytes(size), 2)
        data['File Name'].append(os.path.basename(file_path))
        data['File Size (MB)'].append(size_mb)

        for i, size_range in enumerate(size_ranges):
            if size_range[0] <= size < size_range[1]:
                subfolder_path = subfolder_paths[i]
                shutil.move(file_path, os.path.join(subfolder_path, os.path.basename(file_path)))
                break

    df = pd.DataFrame(data)

    # Write directory, total directory size, subfolder paths, and subfolder sizes to Excel
    with pd.ExcelWriter(output_file_path) as writer:
        df.to_excel(writer, sheet_name='Files', index=False)

        # Write directory information
        df_dir = pd.DataFrame({'Directory Path': [directory_path],
                               'Total Directory Size (GB)': [round(convert_bytes_to_gigabytes(sum(f[1] for f in files)), 2)]})
        df_dir.to_excel(writer, sheet_name='Directory Info', index=False)

        # Write subfolder information
        for i, subfolder_path in enumerate(subfolder_paths):
            subfolder_files = [(os.path.join(subfolder_path, filename), get_file_size(os.path.join(subfolder_path, filename))) for filename in os.listdir(subfolder_path)]
            df_subfolder = pd.DataFrame({'Subfolder Path': [subfolder_path],
                                         'Subfolder Size (MB)': [round(convert_bytes_to_megabytes(sum(f[1] for f in subfolder_files)), 2)]})
            df_subfolder.to_excel(writer, sheet_name=f'Subfolder {i+1} Info', index=False)

# Replace '/your/directory/path' with the actual path of your directory
directory_path = r'E:\YT2024\BHARAT'

# Replace '/desired/output/file/path/output.xlsx' with your desired output Excel file path
output_file_path = r'E:\YT_reorg\YT2024_BHARAT_output.xlsx'

# Specify the size ranges in megabytes
size_ranges = [(0, 15), (15, 200), (200, 4000)]

# Specify the target folder for subfolders
target_folder = r'E:\YT_reorg'

organize_files_and_write_to_excel(directory_path, output_file_path, size_ranges, target_folder)
