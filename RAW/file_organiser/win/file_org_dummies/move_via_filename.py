#Function to Find and Sort Videos by Filename
import os
import logging
import shutil
import time
import sys

# Set up logging
logging.basicConfig(filename='video_scan_log.txt', level=logging.INFO)

def find_and_sort_videos_by_filename(folder_path):
    video_files = []

    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))

        if is_file and has_valid_extension:
            video_files.append(item)

    # Sort the video files by their filenames
    sorted_videos = sorted(video_files)
    return sorted_videos

# # Function to Get Video Duration

# def get_video_duration(video_path):
#     result = os.popen(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}').read()
#     return float(result)

# # # Function to Print and Save Text
# # # This function prints the text to the console and also saves it to a file called "video_transfer_report.txt" in the same folder as the script.
# # # It uses the "a" mode to append to the file, which means that the text will be added to the end of the file.
# # # The encoding is set to "utf-8" to ensure that the text is encoded in UTF-8 format.
# # # The errors='replace' parameter is used to replace any invalid characters with a '?' character.

# def print_and_save(text):
#     print(text)
#     with open('video_transfer_report.txt', 'a', encoding='utf-8') as file:
#         file.write(text + '\n')


def print_and_save(text):
    # Print to console with proper encoding
    sys.stdout.buffer.write(('\n'+ text + '\n').encode(sys.stdout.encoding, errors='replace'))
    sys.stdout.buffer.flush()
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
        # Save to file
    with open('FIle_Transfer_info.txt', 'a' , encoding='utf-8') as file:
        file.write(text + '\n')

    # Redirect stdout to a file
    sys.stdout = open('FIle_Transfer_info.txt', 'w')



# Function to Move Videos Containing "<String>" in Their Names

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
                print_and_save(f"File {video_file} is in use by another process. Retrying...")
                retries += 1
                time.sleep(1) # Wait for 1 second before retrying
            else:
                try:
                    shutil.move(source_path, destination_path)
                    print_and_save(f"Moved {video_file} to {target_folder}")
                    break # Exit the retry loop if the file is successfully moved
                except PermissionError as e:
                    print_and_save(f"Skipped moving {video_file}: {e}")
                    break # Exit the retry loop if the file cannot be moved due to PermissionError
                except OSError as e:
                    print_and_save(f"Failed to move {video_file}: {e}")
                    break # Exit the retry loop if the file cannot be moved due to OSError
                except Exception as e:
                    print_and_save(f"Failed to move {video_file}: {e}")
                    break # Exit the retry loop if an unexpected error occurs
        else:
            print_and_save(f"Failed to move {video_file}: File is still in use after {max_retries} retries")

#Files that remains in the source folder after moving videos containing "<String>" in their names

def report_remaining_files(source_folder):
    remaining_files = [item for item in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, item))]
    with open('remaining_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Remaining files in the source folder:\n\n")
        for file in remaining_files:
            report_file.write(f"\n{file}\n")
            
#Files that moved in the Target folder after moving videos containing "<String>" in their names

def report_Transfered_files(target_folder):
    Moved_files = [item for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))]
    with open('Moved_files_report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write("Moved files in the target folder:\n\n")
        for file in Moved_files:
            report_file.write(f"\n{file}\n")


# Main Function

def main():
    source_folder = r"B:\Test_file_2\source"
    target_folder = r"B:\Test_file_2\target\India Videos"
    new_directory = r"B:\Test_file_2"

    try:
        # Change the current working directory to a different path
        os.chdir(new_directory)
    except OSError as e:
        print_and_save(f"Failed to change directory to {new_directory}: {e}")
        return

    try:
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
    except OSError as e:
        print_and_save(f"Failed to create target folder {target_folder}: {e}")
        return

    # Move video files containing "India" in their names
    move_videos_with_india(source_folder, target_folder)
    
    # Report remaining files in the source folder
    report_remaining_files(source_folder)

    # Report Moved files in the target folder
    report_Transfered_files(target_folder)
if __name__ == "__main__":
    main()

