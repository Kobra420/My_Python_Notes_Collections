from moviepy.editor import VideoFileClip
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

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path, audio=False)  # Skip audio processing
        return clip.duration
    except Exception as e:
        raise VideoProcessingError(f"Error processing file: {file_path}") from e

def format_duration(seconds):
    return seconds

def print_and_save(text):
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
    
    with open('video_scan.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')

def find_and_sort_videos_by_duration(folder_path):
    video_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item)) and
                   item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    video_durations = {}
    for video_file in video_files:
        try:
            duration = get_video_duration(os.path.join(folder_path, video_file))
            if duration is not None:
                video_durations[video_file] = format_duration(duration)
        except VideoProcessingError as e:
            logging.error(e)  # Log the error as per your needs

    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])
    return sorted_videos

def move_files_less_than_duration(sorted_videos, target_path):
    # Inside the move_files_less_than_duration function
    for video, duration in sorted_videos:
        duration_seconds = float(duration) if isinstance(duration, str) else duration
        if duration_seconds < DURATION_THRESHOLD:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(targeted_path, video)

            # Debug information
            print(f"Moving {video} from {source_file} to {destination_file}")
            print(f"\n\nFile exists in source: {os.path.exists(source_file)}")
            print(f"File exists in destination: {os.path.exists(destination_file)}")
      

            max_retries = 3
            retries = 0
            while retries < max_retries:
                try:
                    with open(source_file, 'rb'):
                        pass  # Check if the file can be opened without issues
                except PermissionError:
                    logging.info(f"File {video} is in use by another process. Retrying...")
                    retries += 1
                    time.sleep(1)  # Wait for 1 second before retrying
                else:
                    try:
                        shutil.move(source_file, destination_file)
                        os.remove(source_file)  # Delete the source file after moving it
                        try:
                            logging.info(f"Moved {video} to {target_path}")
                        except UnicodeEncodeError:
                            logging.info(f"Moved {video.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)} to {targeted_path}")
                        break  # Exit the retry loop if the file is successfully moved
                    except PermissionError as e:
                        logging.warning(f"Skipped moving {video}: {e}")
                        break  # Exit the retry loop if the file cannot be moved due to PermissionError
                    except OSError as e:
                        logging.error(f"Failed to move {video}: {e}")
                        break  # Exit the retry loop if the file cannot be moved due to OSError
                    except Exception as e:
                        logging.error(f"Failed to move {video}: {e}")
                        break  # Exit the retry loop if an unexpected error occurs
            else:
                logging.error(f"Failed to move {video}: File is still in use after {max_retries} retries")


# Specify the folder path where the video files are located
folder_path = r"B:\Test File" 
new_directory = r"B:\Test File" 
targeted_path = r"B:\Test File\Target folder Test"

# Change the current working directory to a different path
os.chdir(new_directory) 

# Redirect sys.stdout to a file
with open('video_scan.txt', 'w', encoding='utf-8') as sys_stdout_file:
    sys.stdout = sys_stdout_file

    # Find and sort videos by duration and print them and save them to a text file
    sorted_videos = find_and_sort_videos_by_duration(folder_path) 
    for video, duration in sorted_videos:
        print_and_save(f"{video} - Duration: {format_duration(duration)} seconds")

    # Move files to a new folder based on their duration
    move_files_less_than_duration(sorted_videos, targeted_path)
