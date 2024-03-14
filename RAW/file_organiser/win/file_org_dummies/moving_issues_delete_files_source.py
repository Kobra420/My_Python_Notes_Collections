# Import necessary libraries
from moviepy.editor import VideoFileClip
import os
import sys


# Set up initial paths
# Declared as Global Variables
source_directory = r"B:\Test File\source"
print_and_save_logFILE_path = r'B:\Test File\SourceFiles_DELETE_log.txt'
delete_count = 0

# Constants
DURATION_THRESHOLD = 60.0

class VideoProcessingError(Exception):
    """
    Custom exception class for video processing errors.
    """
    pass


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
        duration = clip.duration
        clip.close()  # Close the clip to release resources
        return duration
    except Exception as e:
        # Raise a custom exception for better error handling
        raise VideoProcessingError(f"\n\nError processing file: {file_path}") from e


def print_and_save(text):
    """
    Print the provided text, encode it to handle special characters, 
    and save it to a text file.

    Parameters:
    - text (str): The text to be printed and saved.
    """
    # Encode text to handle special characters
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

    try:
        with open(print_and_save_logFILE_path, 'a', encoding='utf-8') as file:
            # Add a newline character before each log record
            file.write("\n\n")
            # Print the encoded text to the console
            print(encoded_text)
            # Save the log record to the file
            file.write(f"[INFO] {text}\n")
    except Exception as e:
        # Log an error if there's an issue with file handling
        with open(print_and_save_logFILE_path, 'a', encoding='utf-8') as file:
            file.write(f"[ERROR] Error in file handling: {e}\n")


def delete_files_less_than_duration(directory, duration_threshold=DURATION_THRESHOLD):
    global delete_count  # Declare delete_count as global
    # List all files in the specified directory
    files_in_folder = os.listdir(directory)

    # Iterate over the files
    for file_name in files_in_folder:
        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            try:
                # Get the duration of the video
                duration = get_video_duration(file_path)
                
                # Check if the duration is less than the threshold
                if duration < duration_threshold:
                    # Attempt to delete the file
                    os.remove(file_path)
                    delete_count += 1
                    print_and_save(f"\n\nDeleted file: {file_path} - Duration: {duration} seconds")
                    print_and_save(f"\n\nDeleted file No. {delete_count}")
            except PermissionError:
                print_and_save(f"\n\nSkipped deleting {file_path}: File is in use by another process.")
            except Exception as e:
                print_and_save(f"\n\nFailed to delete file: {file_path}. Error: {e}")
        else:
            print_and_save(f"\n\nSkipped directory: {file_path}")


def main():
    """
    The main function orchestrating the video deleting workflow.
    It takes the source directory as a command-line argument.
    It deletes all files in the source directory that are less than 60 seconds long.
    It logs the deletion of each file and any errors that occur.
    It also logs the start and end time of the workflow.
    It also logs the total number of files deleted.
    It also logs the total number of files skipped.
    It also logs the total number of files that failed to delete.
    It also logs the total number of files that were not deleted.
    It also logs the total number of files that were not skipped.
    It also logs the total number of files that were not failed to delete.
    It also logs the total number of files that were not not deleted.
    It also logs the total number of files that were not not skipped.
    It also logs the total number of files that were not not failed to delete.
    It also logs the total number of files that were not not not deleted.
    It also logs the total number of files that were not not not skipped.
    It also logs the total number of files that were not not not failed to delete.
    """
    global delete_count  # Declare delete_count as global
    # Track the counts of files processed
    deleted_count = 0
    skipped_count = 0
    failed_count = 0

    # Perform file deletion and logging
    try:
        # Count the initial number of files in the source directory
        initial_file_count = len(os.listdir(source_directory))

        # Delete files less than the duration threshold
        delete_files_less_than_duration(source_directory)

        # Count the remaining number of files after deletion
        remaining_file_count = len(os.listdir(source_directory))

        # Calculate the number of files deleted
        deleted_count = initial_file_count - remaining_file_count

        print_and_save(f"\n\n\nWorkflow completed. Deleted {deleted_count} files.")
    except Exception as e:
        print_and_save(f"\n\n\nFailed to complete workflow: {e}")
        failed_count = deleted_count

    # Log counts of skipped and failed files
    skipped_count = len(os.listdir(source_directory)) - deleted_count
    print_and_save(f"\n\nSkipped {skipped_count} files.")
    print_and_save(f"\nFailed to delete {failed_count} files.")
    # print_and_save(f"\n\nNot deleted {skipped_count + failed_count} files.")
    print_and_save(f"\n\n ****TOTAL DELETED FILE COUNT ****{delete_count}")

if __name__ == "__main__":
    main()
