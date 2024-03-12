#Function to Find and Sort Videos by Filename
import os
import logging
import shutil
import time
import sys

# Set up logging
logging.basicConfig(filename='video_scan.log', level=logging.INFO)

def find_and_sort_videos_by_filename(folder_path):
    video_files = []

    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))

        if is_file and has_valid_extension:
            video_files.append((item, get_video_duration(file_path)))

    sorted_videos = sorted(video_files, key=lambda x: (x[1], x[0]))
    return sorted_videos

# Function to Get Video Duration

def get_video_duration(video_path):
    result = os.popen(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}').read()
    return float(result)

# Function to Print and Save Text
def print_and_save(text):
    print(text)
    with open('video_transfer_report.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')

# Function to Move Videos Containing "India" in Their Names

def move_videos_with_india(source_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    video_files = []

    for item in os.listdir(source_folder):
        file_path = os.path.join(source_folder, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
        contains_india = "India" in item

        if is_file and has_valid_extension and contains_india:
            video_files.append(item)

    for video_file in video_files:
        source_path = os.path.join(source_folder, video_file)
        destination_path = os.path.join(target_folder, video_file)

        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                with open(source_path, 'rb'):
                    pass # Check if the file can be opened without issues
            except PermissionError:
                print(f"File {video_file} is in use by another process. Retrying...")
                retries += 1
                time.sleep(1) # Wait for 1 second before retrying
            else:
                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved {video_file} to {target_folder}")
                    break # Exit the retry loop if the file is successfully moved
                except PermissionError as e:
                    print(f"Skipped moving {video_file}: {e}")
                    break # Exit the retry loop if the file cannot be moved due to PermissionError
                except OSError as e:
                    print(f"Failed to move {video_file}: {e}")
                    break # Exit the retry loop if the file cannot be moved due to OSError
                except Exception as e:
                    print(f"Failed to move {video_file}: {e}")
                    break # Exit the retry loop if an unexpected error occurs
        else:
            print(f"Failed to move {video_file}: File is still in use after {max_retries} retries")

# Main Function

def main():
    source_folder = r"B:\Test_file_2\source"
    target_folder = r"B:\Test_file_2\target\India Videos"
    new_directory = r"B:\Test_file_2"

    try:
        # Change the current working directory to a different path
        os.chdir(new_directory)
    except OSError as e:
        print(f"Failed to change directory to {new_directory}: {e}")
        return

    try:
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
    except OSError as e:
        print(f"Failed to create target folder {target_folder}: {e}")
        return

    try:
        # Redirect sys.stdout to a file
        with open('video_transfer_report.txt', 'w', encoding='utf-8') as sys_stdout_file:
            sys.stdout = sys_stdout_file

            # Find and sort videos by filename and print them and save them to a text file
            sorted_videos = find_and_sort_videos_by_filename(source_folder)
            file_number = 0 
            for video, duration in sorted_videos:
                print_and_save(f"{video} - Duration: {duration} - File{file_number}")
                file_number += 1

            # Move video files containing "India" in their names
            move_videos_with_india(source_folder, target_folder)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
