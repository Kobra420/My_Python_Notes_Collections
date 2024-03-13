from moviepy.editor import VideoFileClip
import os
import sys
import time
import shutil
import logging

# Set up logging
logging.basicConfig(
    filename=r'B:\Test File\video_processing_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
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
        clip = VideoFileClip(file_path, audio=False)
        return clip.duration
    except Exception as e:
        raise VideoProcessingError(f"Error processing file: {file_path}") from e

def format_duration(seconds):
    try:
        return f"{float(seconds):.2f} seconds"
    except ValueError:
        return f"{seconds} (Invalid duration)"


def print_and_save(text):
    os.system("echo %cd%")
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
    
    with open(r'B:\Test File\transfer_status.txt', 'a', encoding='utf-8') as file:
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
            logging.error(e)

    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])
    return sorted_videos

def move_files_less_than_duration(sorted_videos, target_path, folder_path):
    for video, duration in sorted_videos:
        try:
            duration_seconds = float(duration.split()[0])  # Extracting the numeric part from the duration string
        except ValueError:
            print_and_save(f"Skipping {video}: Unable to convert duration '{duration}' to float")
            continue

        if duration_seconds < DURATION_THRESHOLD:
            source_file = os.path.join(folder_path, video)
            destination_file = os.path.join(target_path, video)

            print_and_save(f"Moving {video} from {source_file} to {destination_file}")

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
                        logging.info(f"Moved {video} to {target_path}")
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



def report_remaining_files(folder_path):
    remaining_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]
    with open(r'B:\Test File\remaining_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Remaining files in the source folder:\n\n")
        for file in remaining_files:
            report_file.write(f"\n{file}\n")

def report_transferred_files(target_path):
    moved_files = [item for item in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, item))]
    with open(r'B:\Test File\moved_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Moved files in the target folder:\n\n")
        for file in moved_files:
            report_file.write(f"\n{file}\n")

def remove_files_from_source(folder_path):
    # List all files in the specified directory
    files_in_folder = os.listdir(folder_path)
    # Iterate over the files
    for file_name in files_in_folder:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            # Attempt to delete the file
            try:
                os.remove(file_path)
                print_and_save(f"Deleted file: {file_path}")
            except PermissionError:
                print_and_save(f"Skipped deleting {file_path}: File is in use by another process.")
            except Exception as e:
                print_and_save(f"Failed to delete file: {file_path}. Error: {e}")
        else:
            print_and_save(f"Skipped directory: {file_path}")

    # Remove the entire directory and its contents
    try:
        shutil.rmtree(folder_path)
        print_and_save(f"Deleted all files in {folder_path}")
    except Exception as e:
        print_and_save(f"Failed to delete files in {folder_path}. Error: {e}")




def main():
    folder_path = r"B:\Test File\source"
    new_directory = r"B:\Test File"
    target_path = r"B:\Test File\Target"

    os.chdir(new_directory)

    directory_permissions = 0o777  # Read, write, and execute permissions for all
    change_file_permissions(new_directory, directory_permissions)

    original_stdout = sys.stdout
    os.system("echo %cd%")

    with open(r'B:\Test File\transfer_status.txt', 'a', encoding='utf-8') as sys_stdout_file:
        sys.stdout = sys_stdout_file

        sorted_videos = find_and_sort_videos_by_duration(folder_path)
        for video, duration in sorted_videos:
            print_and_save(f"{video} - Duration: {format_duration(duration)}")

        move_files_less_than_duration(sorted_videos, target_path, folder_path)

        report_remaining_files(folder_path)
        report_transferred_files(target_path)

    remove_files_from_source(folder_path)
    sys.stdout = original_stdout

if __name__ == "__main__":
    main()
