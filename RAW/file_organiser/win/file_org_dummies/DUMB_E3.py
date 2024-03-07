from moviepy.editor import VideoFileClip
import os
import sys

# Change the current working directory to a different path
new_directory = r"B:\Test File"  # Remove "example1.txt" from the path
os.chdir(new_directory)

# Specify the folder path where the video files are located
folder_path = r"B:\Test File"
# folder_path = r"P:\GIT4BothOS_Lnx_win\GIT\My_Python_Notes_Collections\RAW\file_organiser\win\file_org_dummies\DUMB_E3"


def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        return clip.duration
    except Exception as e:
        print(f"Error processing file: {file_path}")
        return None
def find_and_sort_videos_by_duration(folder_path):
        video_files = []

    # Get a list of all files and folders in the specified folder_path
        files_and_folders = os.listdir(folder_path)

    # Iterate over each item (file or folder) in the list
        for item in files_and_folders:
            # Check if the current item is a file (not a folder)
            if os.path.isfile(os.path.join(folder_path, item)):
                # Check if the file name ends with any of the specified video file extensions
                if item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                    # If both conditions are met, add the file name to the video_files list
                    video_files.append(item)
        video_durations = {}
        for video_file in video_files:
            duration = get_video_duration(os.path.join(folder_path, video_file))
            if duration is not None:
                video_durations[video_file] = duration      
        sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])     
        return sorted_videos



# Function to print to both console and file
def print_and_save(text):
    # # Print to console with proper encoding
    sys.stdout.buffer.write((text + '\n').encode(sys.stdout.encoding, errors='replace'))
    sys.stdout.buffer.flush()
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
    # # Print to console
    # print(text)
    
    # Save to file
    with open('video_scan.txt', 'a' , encoding='utf-8') as file:
        file.write(text + '\n')

# Redirect stdout to a file
sys.stdout = open('video_scan.txt', 'w')


sorted_videos = find_and_sort_videos_by_duration(folder_path)
for video, duration in sorted_videos:
    print_and_save(f"{video} - Duration: {duration} seconds")
    # print(f"{video} - Duration: {duration} seconds")



# Move files to a new folder based on their duration
# for video, duration in sorted_videos:

import shutil
def move_files_less_than_duration(sorted_videos, target_path):
    for video, duration in sorted_videos:
        if duration < 40.00:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(target_path, video)
            try:
                shutil.move(source_file, destination_file)
                try:
                    print(f"Moved {video} to {target_path}")
                except UnicodeEncodeError:
                    print(f"Moved {video.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)} to {target_path}")
            except PermissionError as e:
                print(f"Failed to move {video}: {e}")
            except OSError as e:
                print(f"Failed to move {video}: {e}")



# Specify the target path where files with duration < 40.00 seconds will be moved
targeted_path = r"B:\Test File\Target folder Test"

# Move files with duration < 40.00 seconds to the targeted path
move_files_less_than_duration(sorted_videos, targeted_path)
