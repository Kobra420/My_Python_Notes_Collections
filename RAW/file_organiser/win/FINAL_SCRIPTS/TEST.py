
import os
# import logging
import sys
import time
# import movingFile_reporting

synthesized_link = str()

def source_link_derivative():
    links = [
    r"E:\YT2024",
    r"E:\YT2024\Anti_Hindu_Bengali",
    r"E:\YT2024\BANGLA1",
    r"E:\YT2024\BANGLA\Vaam Kutta",
    r"E:\YT2024\BANGLA\Vaam Kutta\বামইস্লামিক যাদবপুর",
    r"E:\YT2024\BANGLA\Vaam Kutta\German_SHepherd",
    r"E:\YT2024\BANGLA\tmc",
    r"E:\YT2024\BANGLA\tmc\sondeshkhali",
    r"E:\YT2024\BANGLA\tmc\caa",
    r"E:\YT2024\BANGLA\New folder (3)",
    r"E:\YT2024\BHARAT",
    r"E:\YT2024\BHARAT\প্রানাম ভারতম",
    r"E:\YT2024\BHARAT\The Great DwarakaNath Tegore",
    r"E:\YT2024\BHARAT\Size_102400_inf",
    r"E:\YT2024\BHARAT\Size_10240_102400",
    r"E:\YT2024\BHARAT\S jaishankar\PES University - Golden Jubilee Celebration",
    r"E:\YT2024\BHARAT\modi",
    r"E:\YT2024\BHARAT\Gaganyaan",
    r"E:\YT2024\facts_&_Theories_&_science",
    r"E:\YT2024\facts_&_Theories_&_science\bio",
    r"E:\YT2024\flat earth",
    r"E:\YT2024\korean racism",
    r"E:\YT2024\PD SIR",
    r"E:\YT2024\Ram Krishna Shiva Kaali Kaal",
    r"E:\YT2024\tech_help",
    r"E:\YT2024\west",
    r"E:\YT2024\zukuchacha",
    r"E:\YT2024\zukuchacha\x",
    r"E:\YT2024\zukuchacha\ttiktok",
    r"E:\YT2024\zukuchacha\trump",
    r"E:\YT2024\zukuchacha\open ai",
    r"E:\YT2024\zukuchacha\discord"
]
    global synthesized_link
    for link in links:
        synthesized_link = link
    return synthesized_link



source_folder = synthesized_link
target_folder = r"B:\sorted yt 23\TARGET"
new_directory = r"B:\sorted yt 23\RECORDs_OF_YouTube 2024 downloaded Videos"


head, tail = os.path.split(source_folder)

# report_transferred_files_logFILE_path = r"B:\Test_file_2\transferred_files_log.txt"
# report_remaining_files_logFILE_path = r"B:\Test_file_2\remaining_files_log.txt"
log_file_path = os.path.join(new_directory, f'{tail}.txt')
# TEST_log_file_path = os.path.join(new_directory, 'TEST_log.txt')
# print_and_save_logFILE_path = r'B:\Test_file_2\print_sand_save.txt'


def find_and_sort_videos_by_filename(folder_path):
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
        has_valid_extension = item.lower().endswith(('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.rrc', '.gifv', '.mng', '.mov', '.avi', '.qt', '.wmv', '.yuv', '.rm', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b', '.mod'))
        # contains_india = "India" in item
        if is_file and has_valid_extension: # and contains_india

            video_files.append(item)
            video_count = len(video_files)

        has_valid_extension2 = item.lower().endswith(('.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp', '.tif', '.tiff', '.psd', '.raw', '.arw', '.cr2', '.nrw', '.k25', '.bmp', '.dib', '.heif', '.heic', '.ind', '.indd', '.indt', '.ai', '.eps'))
        if is_file and has_valid_extension2:

            image_files.append(item)
            image_count = len(image_files)

        has_valid_extension3 = item.lower().endswith(('.doc', '.docx', '.html', '.htm', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt', '.log', '.csv', '.xml', '.json', '.yaml', '.ini', '.cfg', '.conf', '.config', '.md', '.markdown','.exe', '.com', '.bat', '.cmd', '.msi', '.dll', '.sys', '.scr', '.vbs', '.vbe', '.js', '.ps1', '.psm1', '.psd1', '.psc1', '.msp', '.mst', '.msp', '.msi', '.msp', '.tar'))
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
        print(f"\n\n****--<<FOLDER_LOCATION>>:--<<{source_folder}>>--****")
        for selected_video in sorted_videos:
            print(f"\n\nSelected video: {selected_video}")
        for selected_image in image_files:
            print(f"\n\nSelected image/pdf: {selected_image}")
        for selected_docs in doc_files:
            print(f"\n\nSelected Docs: {selected_docs}")
    
    # Release sys.stdout to print something else to the screen
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("***Recording complete. Now printing something else to the screen.***")

    # Re-capture stdout for further recording
    with open(log_file_path, 'a', encoding='utf-8') as f:
        sys.stdout = f
        print("******Recording complete. Now printing something else to the screen.******")
    sys.stdout = sys.__stdout__
    time.sleep(2)
    print("*********Recapturing complete. Now printing something else to the screen.*********")

    return sorted_videos, sorted_images, sorted_docs
def main():
    
    # get links from the list of links
    source_link_derivative()
    # Find and sort video files by their filenames
    # sorted_videos = 
    find_and_sort_videos_by_filename(source_folder)

    # # Move the sorted video files to the target folder
    # for video in sorted_videos:
    #     source_path = os.path.join(source_folder, video)
    #     target_path = os.path.join(target_folder, video)
    #     try:
    #         os.rename(source_path, target_path)
    #         # Report the file transfer
    #         movingFile_reporting.log_file_transfer(log_file_path, video, source_path, target_path)
    #     except Exception as e:
    #         logging.error(f"Error moving file: {video} - {e}")

if __name__ == "__main__":
    main()