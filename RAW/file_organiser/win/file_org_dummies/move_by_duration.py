# Import necessary libraries
from moviepy.editor import VideoFileClip
import os
import sys
import time
import shutil
import logging

# Set up logging
logging.basicConfig(
    filename=r'B:\Test File\video_processing_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
DURATION_THRESHOLD = 60.0

class VideoProcessingError(Exception):
    """
    Custom exception class for video processing errors.
    """
    pass

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
    
    # Example usage:
    # \\change_file_permissions(r"B:\\Test File\\source", 0o777)
    """
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


def get_video_duration(file_path):
    """
    Get the duration of a video file.

    Parameters:
    - file_path (str): The path to the video file.

    Returns:
    - float: The duration of the video in seconds.

    Raises:
    - VideoProcessingError: If there's an error processing the file.
    """
    try:
        clip = VideoFileClip(file_path, audio=False)
        return clip.duration
    except Exception as e:
        # Raise a custom exception for better error handling
        raise VideoProcessingError(f"Error processing file: {file_path}") from e

def format_duration(seconds):
    """
    Format the duration in seconds into a human-readable string.

    Parameters:
    - seconds (float): The duration in seconds.

    Returns:
    - str: The formatted duration string.
    """
    try:
        return f"{float(seconds):.2f} seconds"
    except ValueError:
        return f"{seconds} (Invalid duration)"


def print_and_save(text):
    """
    Print the provided text, encode it to handle special characters, 
    and save it to a text file.

    Parameters:
    - text (str): The text to be printed and saved.
    """
    # Encode text to handle special characters
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

    # Save text to a text file and close the file
    with open(r'B:\Test File\transfer_status.txt', 'a', encoding='utf-8') as file:
        # Encode text to handle special characters
        encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        # Print the encoded text to the console
        print(encoded_text)
        file.write(text + '\n')


def find_and_sort_videos_by_duration(folder_path):
    """
    Find and sort video files in a folder based on their durations.

    Parameters:
    - folder_path (str): The path to the folder containing video files.

    Returns:
    - list: A list of tuples containing video file names and their durations, sorted by duration.
    """
    # Get a list of video files in the specified folder
    video_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item)) and
                   item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    # Dictionary to store video durations
    video_durations = {}

    # Iterate through video files, get their durations, and handle errors
    for video_file in video_files:
        try:
            duration = get_video_duration(os.path.join(folder_path, video_file))
            if duration is not None:
                video_durations[video_file] = format_duration(duration)
        except VideoProcessingError as e:
            # Log errors during video processing
            logging.error(e)

    # Sort videos based on their durations
    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])
    return sorted_videos

def move_files_less_than_duration(sorted_videos, target_path, folder_path):
    """
    Move video files with durations less than a threshold to a target path.

    Parameters:
    - sorted_videos (list): A list of tuples containing video file names and their durations, sorted by duration.
    - target_path (str): The path to move the selected video files to.
    - folder_path (str): The path to the folder containing video files.
    """
    # Loop through sorted videos
    for video, duration in sorted_videos:
        try:
            # Extract the numeric part from the duration string
            duration_seconds = float(duration.split()[0])
        except ValueError:
            # Log and skip if duration cannot be converted to float
            print_and_save(f"Skipping {video}: Unable to convert duration '{duration}' to float")
            continue

        # Check if the duration is less than the threshold
        if duration_seconds < DURATION_THRESHOLD:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(target_path, video)

            print_and_save(f"Moving {video} from {source_file} to {destination_file}")

            # Set up retry mechanism for file operations
            max_retries = 3
            retries = 0
            while retries < max_retries:
                try:
                    with open(source_file, 'rb'):
                        pass  # Check if the file can be opened without issues
                except PermissionError:
                    # Retry if the file is in use by another process
                    logging.info(f"File {video} is in use by another process. Retrying...")
                    retries += 1
                    time.sleep(1)  # Wait for 1 second before retrying
                else:
                    try:
                        # Move the file to the destination
                        shutil.move(source_file, destination_file)
                        os.remove(source_file)  # Delete the source file after moving it
                        logging.info(f"Moved {video} to {target_path}")
                        break  # Exit the retry loop if the file is successfully moved
                    except PermissionError as e:
                        # Log a warning if the file cannot be moved due to PermissionError
                        logging.warning(f"Skipped moving {video}: {e}")
                        break  # Exit the retry loop if the file cannot be moved due to PermissionError
                    except OSError as e:
                        # Log an error if the file cannot be moved due to OSError
                        logging.error(f"Failed to move {video}: {e}")
                        break  # Exit the retry loop if the file cannot be moved due to OSError
                    except Exception as e:
                        # Log an error if an unexpected error occurs during file movement
                        logging.error(f"Failed to move {video}: {e}")
                        break  # Exit the retry loop if an unexpected error occurs
            else:
                # Log an error if the file is still in use after maximum retries
                logging.error(f"Failed to move {video}: File is still in use after {max_retries} retries")


def report_remaining_files(folder_path):
    """
    Generate a report of remaining files in the source folder and save it to a text file.

    Parameters:
    - folder_path (str): The path to the source folder.
    """
    # Get a list of remaining files in the source folder
    remaining_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]

    # Write the report to a text file
    with open(r'B:\Test File\remaining_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Remaining files in the source folder:\n\n")
        for file in remaining_files:
            report_file.write(f"\n{file}\n")


def report_transferred_files(target_path):
    """
    Generate a report of moved files in the target folder and save it to a text file.

    Parameters:
    - target_path (str): The path to the target folder.
    """
    # Get a list of moved files in the target folder
    moved_files = [item for item in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, item))]

    # Write the report to a text file
    with open(r'B:\Test File\moved_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Moved files in the target folder:\n\n")
        for file in moved_files:
            report_file.write(f"\n{file}\n")


def remove_files_from_source(folder_path):
    """
    Remove all files and directories from the specified folder.

    Parameters:
    - folder_path (str): The path to the folder to be cleared.
    """
    files_in_folder = os.listdir(folder_path)

    for file_name in files_in_folder:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print_and_save(f"Deleted file: {file_path}")
            except PermissionError as pe:
                print_and_save(f"Skipped deleting {file_path}: File is in use by another process.")
                time.sleep(1)  # Wait for 1 second before continuing to the next iteration
                continue
            except Exception as e:
                print_and_save(f"Failed to delete file: {file_path}. Error: {e}")
        else:
            print_and_save(f"Skipped directory: {file_path}")

    try:
        shutil.rmtree(folder_path)
        print_and_save(f"Deleted all files in {folder_path}")
    except Exception as e:
        print_and_save(f"Failed to delete files in {folder_path}. Error: {e}")


def main():
    """
    The main function orchestrating the video processing workflow.
    """
    # Set up initial paths
    folder_path = r"B:\Test File\source"
    new_directory = r"B:\Test File"
    target_path = r"B:\Test File\Target"

    # Change working directory to the new_directory
    os.chdir(new_directory)

    # Set directory permissions to allow read, write, and execute for all
    directory_permissions = 0o777
    change_file_permissions(new_directory, directory_permissions)

    # Print and save the current directory
    original_stdout = sys.stdout
    os.system("echo %cd%")

    # Redirect stdout to a file for logging
    with open(r'B:\Test File\transfer_status.txt', 'a', encoding='utf-8') as sys_stdout_file:
        sys.stdout = sys_stdout_file

        # Process and print information about sorted videos
        sorted_videos = find_and_sort_videos_by_duration(folder_path)
        for video, duration in sorted_videos:
            print_and_save(f"{video} - Duration: {format_duration(duration)}")

        # Move videos with duration less than a threshold to the target path
        move_files_less_than_duration(sorted_videos, target_path, folder_path)

        # Generate reports for remaining and transferred files
        report_remaining_files(folder_path)
        report_transferred_files(target_path)

    # Remove all files from the source folder
    remove_files_from_source(folder_path)
    
    # Reset stdout to the original value
    sys.stdout = original_stdout

if __name__ == "__main__":
    main()

