import os

def delete_files_in_source(directory):
    # List all files in the specified directory
    files_in_folder = os.listdir(directory)
    
    # Iterate over the files
    for file_name in files_in_folder:
        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            try:
                # Attempt to delete the file
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except PermissionError:
                print(f"Skipped deleting {file_path}: File is in use by another process.")
            except Exception as e:
                print(f"Failed to delete file: {file_path}. Error: {e}")
        else:
            print(f"Skipped directory: {file_path}")

if __name__ == "__main__":
    source_directory = r"B:\Test File\source"
    delete_files_in_source(source_directory)
