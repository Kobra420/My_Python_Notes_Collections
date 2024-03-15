# importing Modules
import os
import logging
import sys

# declaring global variables
# Set directory permissions to allow read, write, and execute for all
directory_permissions = 0o777
source_directory = r"B:\Test File\source"
operational_directory = source_directory       # operational_directory = r"B:\Test File"
# Save text to a text file and close the file at print_and_save(text_to_save, print_and_save_logFILE_path)
print_and_save_logFILE_path = r'B:\Test File\transfer_status.txt'
report_remaining_files_logFILE_path = r'B:\Test File\remaining_files_report.txt'
report_transferred_files_logFILE_path = r'B:\Test File\moved_files_report.txt'
LOG_PATH = r'B:\Test File\video_processing_log.txt'
PATH = print_and_save_logFILE_path

# Set up logging
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def report_remaining_files(source_path, report_remaining_files_logFILE_path):
    """
    Generate a report of remaining files in the source folder and save it to a text file.

    Parameters:
    - source_path (str): The path to the source folder.
    """
    # Get a list of remaining files in the source folder
    remaining_files = [item for item in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, item))]

    # Write the report to a text file
    with open(report_remaining_files_logFILE_path, 'w', encoding='utf-8') as report_file:
        report_file.write("Remaining files in the source folder:\n\n")
        for file in remaining_files:
            report_file.write(f"\n{file}\n")


def report_transferred_files(target_path, report_transferred_files_logFILE_path):
    """
    Generate a report of moved files in the target folder and save it to a text file.

    Parameters:
    - target_path (str): The path to the target folder.
    """
    # Get a list of moved files in the target folder
    moved_files = [item for item in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, item))]

    # Write the report to a text file
    with open(report_transferred_files_logFILE_path, 'w', encoding='utf-8') as report_file:
        report_file.write("Moved files in the target folder:\n\n")
        for file in moved_files:
            report_file.write(f"\n{file}\n")


# Change permission of the source path
def change_file_permissions(directory, permissions):
    """
    Change the permissions of all files in a specified directory.

    Parameters:
    - directory (str): The path to the directory containing the files.
    - permissions (int): The permission code to set for the files.

    Note:
    The function handles potential exceptions during permission changes, 
    as certain files might be protected or the user might not have 
    sufficient privileges. In such cases, an error message is logged.
    
    Example usage:
    change_file_permissions(r"B:\\Test File\\source", 0o777)
    """
    # Change permissions of the specified directory
    try:
        os.chmod(directory, permissions)
        logging.info(f"Permissions of {directory} have been changed to {permissions}")
    except Exception as e:
        # Log an error message if permission change fails
        logging.error(f"Failed to change permissions of {directory}. Error: {e}")

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the item is a file
        if os.path.isfile(file_path):
            try:
                # Attempt to change file permissions
                os.chmod(file_path, permissions)
                logging.info(f"Permissions of {file_path} have been changed to {permissions}")
            except Exception as e:
                # Log an error message if permission change fails
                logging.error(f"Failed to change permissions of {file_path}. Error: {e}")


def print_and_save(text, log_type='info',PATH=print_and_save_logFILE_path):
    """
    Print the provided text, encode it to handle special characters, 
    and save it to a text file.

    Parameters:
    - text (str): The text to be printed and saved.
    - log_type (str): The type of log record ('info', 'warning', 'error').
    """
    # Encode text to handle special characters
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

    try:
        with open(PATH, 'a', encoding='utf-8') as file:
            # Add a newline character before each log record
            file.write("\n\n")
            # Print the encoded text to the console
            print(encoded_text)
            # Save the log record to the file
            file.write(f"[{log_type.upper()}] {text}\n")
    except Exception as e:
        # Log an error if there's an issue with file handling
        logging.error(f"Error in file handling: {e}")

def main():
    # Change working directory to the operational_directory
    os.chdir(operational_directory)
