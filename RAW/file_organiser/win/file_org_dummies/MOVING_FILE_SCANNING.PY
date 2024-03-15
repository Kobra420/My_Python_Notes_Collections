import os
import logging
import sys
import time
import movingFile_reporting

source_folder = r"B:\sorted yt 23\SOURCE\Youtube 2023 August"
target_folder = r"B:\sorted yt 23\TARGET"
new_directory = r"B:\sorted yt 23"
# report_transferred_files_logFILE_path = r"B:\Test_file_2\transferred_files_log.txt"
# report_remaining_files_logFILE_path = r"B:\Test_file_2\remaining_files_log.txt"
log_file_path = os.path.join(new_directory, 'video_MOVE_VIA_NAMES_log.txt')
# TEST_log_file_path = os.path.join(new_directory, 'TEST_log.txt')
# print_and_save_logFILE_path = r'B:\Test_file_2\print_sand_save.txt'

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
        has_valid_extension = item.lower().endswith(('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.rrc', '.gifv', '.mng', '.mov', '.avi', '.qt', '.wmv', '.yuv', '.rm', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.mod'))
        # contains_india = "India" in item
        if is_file and has_valid_extension: # and contains_india
            
            video_files.append(item)

    sorted_videos = sorted(video_files)
    # Redirecting stdout to a file
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        for selected_video in sorted_videos:
            print(f"\n\nSelected video: {selected_video}")
    
    # Release sys.stdout to print something else to the screen
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("***Recording complete. Now printing something else to the screen.***")

    # Re-capture stdout for further recording
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        print("******Recording complete. Now printing something else to the screen.******")
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("*********Recapturing complete. Now printing something else to the screen.*********")

    return sorted_videos
def main():
    # Find and sort video files by their filenames
    # sorted_videos = 
    find_and_sort_videos_by_filename(source_folder)

    # # Move the sorted video files to the target folder
    # for video in sorted_videos:
    #     source_path = os.path.join(source_folder, video)
    #     target_path = os.path.join(target_folder, video)
    #     try:
    #         os.rename(source_path, target_path)
    #         # Report the file transfer
    #         movingFile_reporting.log_file_transfer(log_file_path, video, source_path, target_path)
    #     except Exception as e:
    #         logging.error(f"Error moving file: {video} - {e}")

if __name__ == "__main__":
    main()