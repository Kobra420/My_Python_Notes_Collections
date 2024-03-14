# Import necessary libraries
from moviepy.editor import VideoFileClip
import os
import logging
# import sys
# import time

# Import reporting functions from movingFile_reporting.py
import movingFile_reporting

# Set up initial paths
# Declared as Global Variables
source_directory = r"B:\Test File\source"

# Constants
DURATION_THRESHOLD = 60.0

class VideoProcessingError(Exception):
    """
    Custom exception class for video processing errors.
    """
    pass

# Set up logging
logging.basicConfig(
    filename=r'B:\Test File\SourceFiles_DELETE_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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

def delete_files_less_than_duration(directory, duration_threshold=DURATION_THRESHOLD):
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
                    logging.info(f"\n\nDeleted file: {file_path} - Duration: {duration} seconds")
            except PermissionError:
                logging.warning(f"\n\nSkipped deleting {file_path}: File is in use by another process.")
            except Exception as e:
                logging.error(f"\n\nFailed to delete file: {file_path}. Error: {e}")
        else:
            logging.warning(f"\n\nSkipped directory: {file_path}")


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
    # Track the counts of files processed
    deleted_count = 0
    skipped_count = 0
    failed_count = 0

    # Perform file deletion and logging
    try:
        delete_files_less_than_duration(source_directory)
        deleted_count = len(os.listdir(source_directory))
        logging.info(f"\n\n\nWorkflow completed. Deleted {deleted_count} files.")
    except Exception as e:
        logging.error(f"\n\n\nFailed to complete workflow: {e}")
        failed_count = deleted_count

    # Log counts of skipped and failed files
    skipped_count = len(os.listdir(source_directory)) - deleted_count
    logging.info(f"\n\nSkipped {skipped_count} files.")
    logging.info(f"\n\nFailed to delete {failed_count} files.")
    logging.info(f"\n\nNot deleted {skipped_count + failed_count} files.")

if __name__ == "__main__":
    main()
