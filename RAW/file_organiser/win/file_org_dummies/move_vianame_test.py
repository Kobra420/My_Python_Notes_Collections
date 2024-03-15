import os
# import logging
# import shutil
# import time
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

# # Ensure that the directory exists before setting up logging
# os.makedirs(new_directory, exist_ok=True)

# # Set up logging
# logging.basicConfig(filename=os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt'), level=logging.INFO)


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
    # Redirecting stdout to a file
    with open(os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt'), 'w', encoding='utf-8') as f:
        sys.stdout = f
        for selected_video in sorted_videos:
            print(f"Selected video: {selected_video}")
    return sorted_videos
# test

find_and_sort_videos_by_filename(folder_path =source_folder)
# test = find_and_sort_videos_by_filename(folder_path =source_folder)
# print(test)