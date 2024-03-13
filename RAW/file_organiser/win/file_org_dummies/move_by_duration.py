from moviepy.editor import VideoFileClip
import os
import sys
import time
import shutil
import logging

# Set up logging
# Set up logging for video processing
logging.basicConfig(
    filename='video_scan_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configure logging for permissions changes
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=r"B:\Test File\permissions_log.txt", # Path to the log file for permissions changes
    filemode='a' # Append to the file if it exists
)

# Constants
DURATION_THRESHOLD = 60.0

class VideoProcessingError(Exception):
    pass



def change_file_permissions(directory, permissions):
    """
    Change the permissions of all files in a specified directory.

    Parameters:
    - directory (str): The path to the directory containing the files.
    - permissions (int): The permission code to set for the files.
    """
    # Loop through the list of files in the directory and change their permissions
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                os.chmod(file_path, permissions)
                logging.info(f"Permissions of {file_path} have been changed to {permissions}")
            except Exception as e:
                logging.error(f"Failed to change permissions of {file_path}. Error: {e}")

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
    
    with open('transfer_status.txt', 'a', encoding='utf-8') as file:
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

def move_files_less_than_duration(sorted_videos, target_path, folder_path):
    # Inside the move_files_less_than_duration function
    for video, duration in sorted_videos:
        duration_seconds = float(duration) if isinstance(duration, str) else duration
        if duration_seconds < DURATION_THRESHOLD:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(target_path, video)

            # Debug information
            # print(f"Moving {video} from {source_file} to {destination_file}")
            print_and_save(f"Moving {video} from {source_file} to {destination_file}")
            # print(f"\n\nFile exists in source: {os.path.exists(source_file)}")
            print_and_save(f"\n\nFile exists in source: {os.path.exists(source_file)}")
            # print(f"File exists in destination: {os.path.exists(destination_file)}")
            print_and_save(f"File exists in destination: {os.path.exists(destination_file)}")
      

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
                            logging.info(f"Moved {video.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)} to {target_path}")
                        # break  # Exit the retry loop if the file is successfully moved
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

#Files that remains in the source folder after moving videos containing "<String>" in their names

def report_remaining_files(folder_path):
    remaining_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]
    with open('remaining_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Remaining files in the source folder:\n\n")
        for file in remaining_files:
            report_file.write(f"\n{file}\n")
            
#Files that moved in the Target folder after moving videos containing "<String>" in their names

def report_Transfered_files(targeted_path):
    Moved_files = [item for item in os.listdir(targeted_path) if os.path.isfile(os.path.join(targeted_path, item))]
    with open('Moved_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Moved files in the target folder:\n\n")
        for file in Moved_files:
            report_file.write(f"\n{file}\n")
            

# Main Function

def main():
    # Specify the folder path where the video files are located
    folder_path = r"B:\Test File\source"
    new_directory = r"B:\Test File" 
    targeted_path = r"B:\Test File\Target"

    # Change the current working directory to a different path
    os.chdir(new_directory) 

    # Redirect sys.stdout to a file
    original_stdout = sys.stdout # Store the original sys.stdout
    with open('video_scan.txt', 'w', encoding='utf-8') as sys_stdout_file:
        sys.stdout = sys_stdout_file

        # Find and sort videos by duration and print them and save them to a text file
        sorted_videos = find_and_sort_videos_by_duration(folder_path) 
        for video, duration in sorted_videos:
            print_and_save(f"{video} - Duration: {format_duration(duration)} seconds")

        # Move files to a new folder based on their duration
        move_files_less_than_duration(sorted_videos, targeted_path, folder_path)
    # Restore the original sys.stdout
    sys.stdout = original_stdout

    # Example usage of change_file_permissions
    directory = new_directory
    permissions = 0o777 # Read, write, and execute permissions for all
    change_file_permissions(directory, permissions)

if __name__ == "__main__":
    main()