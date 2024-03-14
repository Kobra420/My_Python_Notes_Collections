# junk functons from the scripts of file movings and their dummies

# move_files_less_than_duration(sorted_videos, target_path, folder_path)
# def move_files_less_than_duration(sorted_videos, target_path, folder_path):
#     """
#     Move video files with durations less than a threshold to a target path.

#     Parameters:
#     - sorted_videos (list): A list of tuples containing video file names and their durations, sorted by duration.
#     - target_path (str): The path to move the selected video files to.
#     - folder_path (str): The path to the folder containing video files.
#     """
#     # Loop through sorted videos
#     for video, duration in sorted_videos:
#         try:
#             # Extract the numeric part from the duration string
#             duration_seconds = float(duration.split()[0])
#         except ValueError:
#             # Log and skip if duration cannot be converted to float
#             print_and_save(f"Skipping {video}: Unable to convert duration '{duration}' to float")
#             continue

#         # Check if the duration is less than the threshold
#         if duration_seconds < DURATION_THRESHOLD:
#             source_file = os.path.join(folder_path, video)
#             destination_file = os.path.join(target_path, video)

#             print_and_save(f"Moving {video} from {source_file} to {destination_file}")

#             # Set up retry mechanism for file operations
#             max_retries = 3
#             retries = 0
#             while retries < max_retries:
#                 try:
#                     with open(source_file, 'rb'):
#                         pass  # Check if the file can be opened without issues
#                 except PermissionError:
#                     # Retry if the file is in use by another process
#                     logging.info(f"File {video} is in use by another process. Retrying...")
#                     retries += 1
#                     time.sleep(1)  # Wait for 1 second before retrying
#                 else:
#                     try:
#                         # Move the file to the destination
#                         shutil.move(source_file, destination_file)
#                         os.remove(source_file)  # Delete the source file after moving it
#                         logging.info(f"Moved {video} to {target_path}")
#                         break  # Exit the retry loop if the file is successfully moved
#                     except PermissionError as e:
#                         # Log a warning if the file cannot be moved due to PermissionError
#                         logging.warning(f"Skipped moving {video}: {e}")
#                         break  # Exit the retry loop if the file cannot be moved due to PermissionError
#                     except OSError as e:
#                         # Log an error if the file cannot be moved due to OSError
#                         logging.error(f"Failed to move {video}: {e}")
#                         break  # Exit the retry loop if the file cannot be moved due to OSError
#                     except Exception as e:
#                         # Log an error if an unexpected error occurs during file movement
#                         logging.error(f"Failed to move {video}: {e}")
#                         break  # Exit the retry loop if an unexpected error occurs
#             else:
#                 # Log an error if the file is still in use after maximum retries
#                 logging.error(f"Failed to move {video}: File is still in use after {max_retries} retries")