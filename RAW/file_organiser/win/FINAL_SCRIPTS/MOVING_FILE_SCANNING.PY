# importing Modules
import os
import sys
import time

# importing custom module
import data


# Global Variable declarations
links_2 = data.links_2024
source_folder = str()
new_directory = str()
# log_file_list = list()  # Initialize list() for future extentions of this operation , currently unused.


def get_links(source_folder, new_directory):
    """
    Generate source folder and log file path for a given identifier.

    Parameters:
    - source_folder (str): The source folder containing video files.
    - new_directory (str): The directory for storing log files.
    - identifier (str): An identifier to distinguish between sets of links.

    Returns:
    - tuple: A tuple containing the source folder and log file path.
    """
    new_directory = r"B:\sorted yt 23\RECORDs_OF_YouTube 2024 downloaded Videos"

    head, tail = os.path.split(source_folder)

    log_file_path = os.path.join(new_directory, f'{tail}.txt')
    return source_folder, log_file_path




def find_and_sort_videos_by_filename(folder_path, log_file_path):
    """
    Find and sort video files by their filenames.

    Parameters:
    - folder_path (str): The path to the folder containing video files.

    Returns:
    - list: A list of video filenames sorted alphabetically.
    """

    
    # initializations
    video_files = []  # Initialize video_files before the for loop
    image_files = []  # Initialize image_files before the for loop
    doc_files = []    # Initialize doc_files before the for loop
    video_count = 0   # Initialize video_count before the if conditions
    image_count = 0   # Initialize doc_count before the if conditions
    doc_count = 0     # Initialize doc_count before the if conditions
    
    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)
        is_file = os.path.isfile(file_path)
        has_valid_extension = item.lower().endswith(('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.rrc', '.gifv',
                                                     '.mng', '.mov', '.avi', '.qt', '.wmv', '.yuv', '.rm', '.asf',
                                                     '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe',
                                                     '.mpv', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv',
                                                     '.f4v', '.f4p', '.f4a', '.f4b', '.mod'))
        # contains_india = "India" in item
        if is_file and has_valid_extension: # and contains_india

            video_files.append(item)
            video_count = len(video_files)

        has_valid_extension2 = item.lower().endswith(('.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', 
                                                      '.pjp', '.png', '.svg', '.webp', '.tif', '.tiff', '.psd', '.raw', 
                                                      '.arw', '.cr2', '.nrw', '.k25', '.bmp', '.dib', '.heif', '.heic',
                                                      '.ind', '.indd', '.indt', '.ai', '.eps'))
        if is_file and has_valid_extension2:

            image_files.append(item)
            image_count = len(image_files)

        has_valid_extension3 = item.lower().endswith(('.doc', '.docx', '.html', '.htm', '.odt', '.pdf', '.xls', '.xlsx',
                                                      '.ods', '.ppt', '.pptx', '.txt', '.log', '.csv', '.xml', '.json', 
                                                      '.yaml', '.ini', '.cfg', '.conf', '.config', '.md', '.markdown','.exe',
                                                      '.com', '.bat', '.cmd', '.msi', '.dll', '.sys', '.scr', '.vbs', '.vbe',
                                                      '.js', '.ps1', '.psm1', '.psd1', '.psc1', '.msp',
                                                      '.mst', '.msp', '.msi', '.msp', '.tar'))
        if is_file and has_valid_extension3:

            doc_files.append(item)
            doc_count = len(doc_files)

    sorted_videos = sorted(video_files)
    sorted_images = sorted(image_files)
    sorted_docs = sorted(doc_files)
    total_items = video_count + image_count + doc_count
    # Redirecting stdout to a file
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        print(f"\n+++--<<Total number of videos found: {video_count}>>--+++")
        print(f"\n+++--<<Total number of images found: {image_count}>>--+++")
        print(f"\n+++--<<Total number of Docs found: {doc_count}>>--+++")
        print(f"\n+++--<<Total number ITEMS found: {total_items}>>--+++")
        print(f"\n\n****--<<FOLDER_LOCATION>>:--<<{folder_path}>>--****")
        for selected_video in sorted_videos:
            print(f"\n\nSelected video: {selected_video}")
        for selected_image in image_files:
            print(f"\n\nSelected image/pdf: {selected_image}")
        for selected_docs in doc_files:
            print(f"\n\nSelected Docs: {selected_docs}")
    
    # Release sys.stdout to print something else to the screen
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("\n***Recording complete. Now printing something else to the screen.***")

    # Re-capture stdout for further recording
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        print("\n******Recording complete. Now printing something else to the screen.******")
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("\n*********Recapturing complete. Now printing something else to the screen.*********")

    return sorted_videos, sorted_images, sorted_docs
def main():
    for link in links_2:
        source_folder, log_file_path = get_links(link, new_directory)
        find_and_sort_videos_by_filename(source_folder, log_file_path)
if __name__ == "__main__":
    main()

# for link in links:
#     source_folder, log_file_path = get_links(link, new_directory)
#     find_and_sort_videos_by_filename(source_folder, log_file_path)
