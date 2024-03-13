# Import necessary libraries
from moviepy.editor import VideoFileClip
import os
import logging
import sys
import time

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
        raise VideoProcessingError(f"Error processing file: {file_path}") from e

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
                    logging.info(f"Deleted file: {file_path} - Duration: {duration} seconds")
            except PermissionError:
                logging.warning(f"Skipped deleting {file_path}: File is in use by another process.")
            except Exception as e:
                logging.error(f"Failed to delete file: {file_path}. Error: {e}")
        else:
            logging.warning(f"Skipped directory: {file_path}")

if __name__ == "__main__":
    source_directory = r"B:\Test File\source"
    delete_files_less_than_duration(source_directory)
