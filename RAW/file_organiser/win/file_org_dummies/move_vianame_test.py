import os
import logging
import sys
import movingFile_reporting

source_folder = r"B:\Test_file_2\source"
target_folder = r"B:\Test_file_2\target\India_Videos"
new_directory = r"B:\Test_file_2"
report_transferred_files_logFILE_path = r"B:\Test_file_2\transferred_files_log.txt"
report_remaining_files_logFILE_path = r"B:\Test_file_2\remaining_files_log.txt"
log_file_path = os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt')
TEST_log_file_path = os.path.join(new_directory, 'TEST_log.txt')
print_and_save_logFILE_path = r'B:\Test_file_2\print_sand_save.txt'



def find_and_sort_videos_by_filename(folder_path):
    """
    Find and sort video files by their filenames.

    Parameters:
    - folder_path (str): The path to the folder containing video files.

    Returns:
    - list: A list of video filenames sorted alphabetically.
    """
    video_files = []

    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
        contains_india = "India" in item
        if is_file and has_valid_extension and contains_india:
            video_files.append(item)

    sorted_videos = sorted(video_files)
    # Redirecting stdout to a file
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        for selected_video in sorted_videos:
            print(f"Selected video: {selected_video}")
    
    # Release sys.stdout to print something else to the screen
    sys.stdout = sys.__stdout__
    print("Recording complete. Now printing something else to the screen.")

    # Re-capture stdout for further recording
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        print("Recording complete. Now printing something else to the screen.")
    sys.stdout = sys.__stdout__
    print("Recapturing complete. Now printing something else to the screen.")

    return sorted_videos



# Adding logging for errors
try:
    find_and_sort_videos_by_filename(folder_path=source_folder)
    movingFile_reporting.print_and_save("Videos sorted successfully.",PATH = print_and_save_logFILE_path)
except Exception as e:
    logging.error(f"An error occurred: {str(e)}", TEST_log_file_path)
logging.info("Videos sorted successfully.", TEST_log_file_path)
