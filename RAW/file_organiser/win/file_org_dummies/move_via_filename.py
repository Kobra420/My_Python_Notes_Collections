# Comparing to FILE1 and write a code which moves video files containing file names "JSD " to a desired  folder
import moviepy.editor # as mp
import os
import sys
import time
import shutil
import logging

# Set up logging
logging.basicConfig(filename='video_scan.log', level=logging.INFO)

# Constants
DURATION_THRESHOLD = 60.0

class VideoProcessingError(Exception):
    pass

def print_and_save(text):
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
    
    with open('video_transfer_report.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


# Function to find and sort videos by filename containing "India"
def find_and_sort_videos_by_filename(folder_path):
    video_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item)) and
                   item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')) and "India" in item]

    sorted_videos = sorted(video_files)
    return sorted_videos



# Function to move video files containing "Strings" in their names
# move video files containing "Strings" in their names
# Function to move video files containing "JSD" in their names
def move_videos_with_jsd(source_folder, target_folder):
    video_files = []

    for item in os.listdir(source_folder):
        file_path = os.path.join(source_folder, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))
        contains_jsd = "India" in item

        if is_file and has_valid_extension and contains_jsd:
            video_files.append(item)

    for video_file in video_files:
        source_path = os.path.join(source_folder, video_file)
        destination_path = os.path.join(target_folder, video_file)

        # Debug information
        print(f"Moving {video_file} from {source_path} to {destination_path}")
        print(f"\n\nFile exists in source: {os.path.exists(source_path)}")
        print(f"File exists in destination: {os.path.exists(destination_path)}")

        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                with open(source_path, 'rb'):
                    pass  # Check if the file can be opened without issues
            except PermissionError:
                logging.info(f"File {video_file} is in use by another process. Retrying...")
                retries += 1
                time.sleep(1)  # Wait for 1 second before retrying
            else:
                try:
                    shutil.move(source_path, destination_path)
                    os.remove(source_path)  # Delete the source file after moving it
                    logging.info(f"Moved {video_file} to {target_folder}")
                    break  # Exit the retry loop if the file is successfully moved
                except PermissionError as e:
                    logging.warning(f"Skipped moving {video_file}: {e}")
                    break  # Exit the retry loop if the file cannot be moved due to PermissionError
                except OSError as e:
                    logging.error(f"Failed to move {video_file}: {e}")
                    break  # Exit the retry loop if the file cannot be moved due to OSError
                except Exception as e:
                    logging.error(f"Failed to move {video_file}: {e}")
                    break  # Exit the retry loop if an unexpected error occurs
        else:
            logging.error(f"Failed to move {video_file}: File is still in use after {max_retries} retries")



source_folder = r"B:\Test_file_2\source"
target_folder = r"B:\Test_file_2\target\JSD Videos"
new_directory = r"B:\Test_file_2"

# Change the current working directory to a different path
os.chdir(new_directory) 

# Specify the source and target folders
# Specify the folder path where the video files are located

# Redirect sys.stdout to a file
with open('video_transfer_report.txt', 'w', encoding='utf-8') as sys_stdout_file:
    sys.stdout = sys_stdout_file

    # Find and sort videos by duration and print them and save them to a text file
    sorted_videos = find_and_sort_videos_by_filename(target_folder)
    i = 0 
    for video, duration in sorted_videos:
        print_and_save(f"{sorted_videos} - File{i}")
        i+=i


# Move video files containing "JSD" in their names
move_videos_with_jsd(source_folder, target_folder)

