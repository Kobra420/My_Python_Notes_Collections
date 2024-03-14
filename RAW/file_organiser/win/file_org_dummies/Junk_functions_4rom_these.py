# junk functons from the scripts of file movings and their dummies
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Function 1 - move_files_less_than_duration

# # This function takes in a list of tuples containing video file names and their durations, sorted by duration.
# # It then moves the video files with durations less than a threshold to a target path.
# # The threshold is set to 30 seconds.
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


# Function 2 - remove_from_source_folder

    # Remove all files from the source folder
    # remove_files_from_source(folder_path)

# Remove all files from the source folder

# def remove_files_from_source(folder_path):
#     """
#     Remove all files and directories from the specified folder.

#     Parameters:
#     - folder_path (str): The path to the folder to be cleared.
#     """
#     files_in_folder = os.listdir(folder_path)

#     for file_name in files_in_folder:
#         file_path = os.path.join(folder_path, file_name)

#         if os.path.isfile(file_path):
#             try:
#                 # Attempt to remove the file
#                 os.remove(file_path)
#                 print_and_save(f"Deleted file: {file_path}")
#             except PermissionError as pe:
#                 # Log a message if the file is in use by another process
#                 print_and_save(f"Skipped deleting {file_path}: File is in use by another process. Error: {pe}", log_type='warning')
#                 time.sleep(1)  # Wait for 1 second before continuing to the next iteration
#                 continue
#             except Exception as e:
#                 # Log an error message if file deletion fails
#                 print_and_save(f"Failed to delete file: {file_path}. Error: {e}", log_type='error')
#         else:
#             # Log a message for skipped directories
#             print_and_save(f"Skipped directory: {file_path}")

#     try:
#         # Attempt to remove the entire folder
#         shutil.rmtree(folder_path)
#         print_and_save(f"Deleted all files in {folder_path}")
#     except PermissionError as pe:
#         # Log a message if folder deletion fails due to permissions
#         print_and_save(f"Failed to delete files in {folder_path}. PermissionError: {pe}", log_type='error')
#     except Exception as e:
#         # Log an error message if folder deletion fails
#         print_and_save(f"Failed to delete files in {folder_path}. Error: {e}", log_type='error')

