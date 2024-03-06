from moviepy.editor import VideoFileClip
import os

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        return clip.duration
    except Exception as e:
        print(f"Error processing file: {file_path}")
        return None
def find_and_sort_videos_by_duration(folder_path):
    video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    video_durations = {}
    for video_file in video_files:
        duration = get_video_duration(os.path.join(folder_path, video_file))
        if duration is not None:
            video_durations[video_file] = duration

    sorted_videos = sorted(video_durations.items(), key=lambda x: x[1])

    return sorted_videos

# Specify the folder path where the video files are located
folder_path = "path/to/your/video/folder"

sorted_videos = find_and_sort_videos_by_duration(folder_path)