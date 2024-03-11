# Comparing to FILE1 and write a code which moves video files containing file names "JSD " to a desired  folder
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
# Function to move video files containing "Strings" in their names
# move video files containing "Strings" in their names
def move_videos_with_jsd(source_folder, target_folder):
    video_files = [item for item in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, item)) and
                   item.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')) and "JSD" in item]

    for video_file in video_files:
        source_path = os.path.join(source_folder, video_file)
        destination_path = os.path.join(target_folder, video_file)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {video_file} to {target_folder}")
        except (shutil.Error, PermissionError, OSError) as e:
            print(f"Failed to move {video_file}: {e}")

# Specify the source and target folders
source_folder = r"B:\Test File"
target_folder = r"B:\Test File\JSD Videos"

# Move video files containing "JSD" in their names
move_videos_with_jsd(source_folder, target_folder)
