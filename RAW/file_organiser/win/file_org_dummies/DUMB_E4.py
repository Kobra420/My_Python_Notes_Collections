from moviepy.editor import VideoFileClip
import os
import sys
import shutil

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        return clip.duration
    except Exception as e:
        print(f"Error processing file: {file_path}")
        return None

def find_and_sort_videos_by_duration(folder_path):
    video_files = []
    
    files_and_folders = os.listdir(folder_path)
    
    for item in files_and_folders:
        if os.path.isfile(os.path.join(folder_path, item)):
            if item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                video_files.append(item)
    
    video_durations = {}
    for video_file in video_files:
        duration = get_video_duration(os.path.join(folder_path, video_file))
        if duration is not None:
            video_durations[video_file] = duration
    
    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])
    
    return sorted_videos

def print_and_save(text):
    encoded_text = text.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
    print(encoded_text)
    
    with open('video_scan.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')

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
            except Exception as e:
                print(f"Failed to move {video}: {e}")

folder_path = r"B:\Test File"
new_directory = r"B:\Test File"
targeted_path = r"B:\Test File\Target folder Test"

os.chdir(new_directory)
sys.stdout = open('video_scan.txt', 'w')

sorted_videos = find_and_sort_videos_by_duration(folder_path)
for video, duration in sorted_videos:
    print_and_save(f"{video} - Duration: {duration} seconds")

move_files_less_than_duration(sorted_videos, targeted_path)
