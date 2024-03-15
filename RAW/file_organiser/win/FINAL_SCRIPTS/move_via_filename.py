import os
import logging
import shutil
import time
import sys

# Custom module for reporting functions
import movingFile_reporting

# Set up initial paths
# Declared as Global Variables
source_folder = r"B:\Test_file_2\source"
target_folder = r"B:\Test_file_2\target\India_Videos"
new_directory = r"B:\Test_file_2"
report_transferred_files_logFILE_path = r"B:\Test_file_2\transferred_files_log.txt"
report_remaining_files_logFILE_path = r"B:\Test_file_2\remaining_files_log.txt"
log_file_path = os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt')

# Ensure that the directory exists before setting up logging
os.makedirs(new_directory, exist_ok=True)

# Set up logging
logging.basicConfig(filename=os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt'), level=logging.INFO)


def find_and_sort_videos_by_filename(folder_path):
    """
    Find and sort video files by their filenames.

    Parameters:
    - folder_path (str): The path to the folder containing video files.

    Returns:
    - list: A list of video filenames sorted alphabetically.

    """
    video_files = []

    # Iterate through files in the folder
    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
        contains_india = "India" in item
        # Check if the item is a file and has a valid video file extension
        if is_file and has_valid_extension and contains_india:
            video_files.append(item)

    # Sort the video files by their filenames
    sorted_videos = sorted(video_files)
    return sorted_videos


def print_and_save(text, file_obj):
    # Print to console with proper encoding
    sys.stdout.buffer.write(('\n' + text + '\n').encode(sys.stdout.encoding, errors='replace'))
    sys.stdout.buffer.flush()
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)

    # Save to file
    file_obj.write(text + '\n')


# Function to Move Videos Containing "<String>" in Their Names
def move_videos_with_india(source_folder, target_folder, log_file):
    """
    Move video files from the source folder to the target folder if their filenames contain "India".

    Parameters:
    - source_folder (str): The path to the source folder containing video files.
    - target_folder (str): The path to the target folder where the videos will be moved.
    - log_file (file object): The file object for writing logs.
    """
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    video_files = []

    # Iterate through files in the source folder
    for item in os.listdir(source_folder):
        file_path = os.path.join(source_folder, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
        contains_india = "India" in item

        # Check if the item is a file, has a valid video file extension, and contains "India" in the filename
        if is_file and has_valid_extension and contains_india:
            video_files.append(item)

    # Move each video file containing "India" to the target folder
    for video_file in video_files:
        source_path = os.path.join(source_folder, video_file)
        destination_path = os.path.join(target_folder, video_file)

        # Set up retry mechanism for file operations
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                # Check if the file can be opened without issues
                with open(source_path, 'rb'):
                    pass
            except PermissionError:
                logging.warning(f"File {video_file} is in use by another process. Retrying...")
                retries += 1
                time.sleep(1)  # Wait for 1 second before retrying
            else:
                try:
                    # Move the file to the destination
                    shutil.move(source_path, destination_path)
                    print_and_save(f"\n\nMoved {video_file} to {target_folder}", log_file)
                    logging.info(f"\n\nMoved {video_file} to {target_folder}")
                    break  # Exit the retry loop if the file is successfully moved
                except PermissionError as e:
                    logging.error(f"\n\nSkipped moving {video_file}: {e}")
                    break  # Exit the retry loop if the file cannot be moved due to PermissionError
                except OSError as e:
                    logging.error(f"\n\nFailed to move {video_file}: {e}")
                    break  # Exit the retry loop if the file cannot be moved due to OSError
                except Exception as e:
                    logging.error(f"\n\nFailed to move {video_file}: {e}")
                    break  # Exit the retry loop if an unexpected error occurs
        else:
            logging.error(f"\n\nFailed to move {video_file}: File is still in use after {max_retries} retries")


# Main Function
def main():
    try:
        # Change the current working directory to a different path
        os.chdir(new_directory)
    except OSError as e:
        logging.error(f"\n\nFailed to change directory to {new_directory}: {e}")
        return

    try:
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
    except OSError as e:
        logging.error(f"\n\nFailed to create target folder {target_folder}: {e}")
        return

    # Open the log file in append mode
    with open(os.path.join(new_directory, 'FIle_Transfer_VIA_NAME_info.txt'), 'a', encoding='utf-8') as log_file:
        # Move video files containing "India" in their names
        move_videos_with_india(source_folder, target_folder, log_file)

   # Report remaining files in the source folder
        movingFile_reporting.report_remaining_files(source_folder, report_remaining_files_logFILE_path)

        # Report Moved files in the target folder
        movingFile_reporting.report_transferred_files(target_folder, report_transferred_files_logFILE_path)
    logging.info("\n\n\nThere are no Errors/warings in the \\Output")


if __name__ == "__main__":
    main()
