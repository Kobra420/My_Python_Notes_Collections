"""
This script imports necessary libraries and functions for managing video files and performing file operations.
"""

from moviepy.editor import VideoFileClip  # Library for working with video files
import os  # Operating system module for file handling
import shutil  # Module for high-level file operations
import time  # Module for time-related functions

import moving_issues_delete_files_source  # Custom module for deleting files based on duration
import movingFile_reporting  # Custom module for reporting functions

# Set up initial paths GLOBAL VARIABLE
folder_path = r"B:\Test File\source"  # Path to the source folder
target_path = r"B:\Test File\Target"  # Path to the target folder
report_remaining_files_logFILE_path = r'B:\Test File\remaining_files_report.txt' # PATH OF LOG_TXT OF REMAINING FILES AT SOURCE FOLDER
report_transferred_files_logFILE_path = r'B:\Test File\moved_files_report.txt'   # PATH OF LOG_TXT OF MOVED FILES AT TARGET FOLDER

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
        # Attempt to create a VideoFileClip object
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
        # Format the duration with two decimal places
        return f"{float(seconds):.2f} seconds"
    except ValueError:
        # Handle invalid duration values
        return f"{seconds} (Invalid duration)"


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
            # Attempt to get the duration of the video
            duration = get_video_duration(os.path.join(folder_path, video_file))
            
            # Check if the duration is not None before storing it
            if duration is not None:
                video_durations[video_file] = format_duration(duration)
        except VideoProcessingError as e:
            # Log errors during video processing
            movingFile_reporting.logging.error(e)

    # Sort videos based on their durations
    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])
    return sorted_videos


def copy_files_less_than_duration(sorted_videos, target_path, folder_path):
    """
    Copy video files with durations less than a threshold to a target path.

    Parameters:
    - sorted_videos (list): A list of tuples containing video file names and their durations, sorted by duration.
    - target_path (str): The path to copy the selected video files to.
    - folder_path (str): The path to the folder containing video files.
    """
    # Loop through sorted videos
    for video, duration in sorted_videos:
        try:
            # Extract the numeric part from the duration string
            duration_seconds = float(duration.split()[0])
        except ValueError:
            # Log and skip if duration cannot be converted to float
            movingFile_reporting.print_and_save(f"Skipping {video}: Unable to convert duration '{duration}' to float")
            continue

        # Check if the duration is less than the threshold
        if duration_seconds < DURATION_THRESHOLD:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(target_path, video)

            movingFile_reporting.print_and_save(f"Copying {video} from {source_file} to {destination_file}")

            # Set up retry mechanism for file operations
            max_retries = 3
            retries = 0
            while retries < max_retries:
                try:
                    # Copy the file to the destination
                    shutil.copy2(source_file, destination_file)
                    movingFile_reporting.logging.info(f"Copied {video} to {target_path}")
                    
                    # Close the clip to release resources
                    clip = VideoFileClip(source_file, audio=False)
                    clip.close()
                    
                    break  # Exit the retry loop if the file is successfully copied
                except PermissionError:
                    # Retry if the file is in use by another process
                    movingFile_reporting.logging.info(f"File {video} is in use by another process. Retrying...")
                    retries += 1
                    time.sleep(1)  # Wait for 1 second before retrying
                except Exception as e:
                    # Log an error if an unexpected error occurs during file copying
                    movingFile_reporting.logging.error(f"Failed to copy {video}: {e}")
                    break  # Exit the retry loop if an unexpected error occurs
            else:
                # Log an error if the file is still in use after maximum retries
                movingFile_reporting.logging.error(f"Failed to copy {video}: File is still in use after {max_retries} retries")



def main():
    """
    The main function orchestrating the video processing workflow.
    """

    # Print and save the current directory
    current_directory = os.getcwd()
    movingFile_reporting.print_and_save(f"\n\nCurrent working directory: {current_directory}\n\n")


    # Redirect stdout to a file for logging
    with open(r'B:\Test File\transfer_status.txt', 'a', encoding='utf-8'):

        # Process and print information about sorted videos
        sorted_videos = find_and_sort_videos_by_duration(folder_path)
        for video, duration in sorted_videos:
            movingFile_reporting.print_and_save(f"\n\n{video} - Duration: {format_duration(duration)}\n\n")

        # Copy videos with duration less than a threshold to the target path
        copy_files_less_than_duration(sorted_videos, target_path, folder_path)


if __name__ == "__main__":
    main()
    
    # Call the imported function from Script 2
    
    source_directory = folder_path      # source_directory = r"B:\Test File\source"
    movingFile_reporting.main()
    
    # delete_files_less_than_duration(source_directory)
    moving_issues_delete_files_source.delete_files_less_than_duration(source_directory)
    
    # Generate reports for remaining and transferred files
    movingFile_reporting.report_remaining_files(folder_path, report_remaining_files_logFILE_path)
    movingFile_reporting.report_transferred_files(target_path, report_transferred_files_logFILE_path)
    moving_issues_delete_files_source.main()
