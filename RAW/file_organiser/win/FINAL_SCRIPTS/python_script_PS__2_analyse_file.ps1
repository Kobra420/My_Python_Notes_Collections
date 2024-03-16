# PowerShell script to run python_script1.py and python_script2.py

# Define the paths to the Python scripts
$script1Path = "C:\Users\biswa\OneDrive\Documents\GIT\GIT_main\My_Python_Notes_Collections\RAW\file_organiser\win\FINAL_SCRIPTS\MOVING_FILE_SCANNING.PY"
$script2Path = "C:\Users\biswa\OneDrive\Documents\GIT\GIT_main\My_Python_Notes_Collections\RAW\file_organiser\win\FINAL_SCRIPTS\MOVING_FILE_SCANNING_2.PY"

# Run python_script1.py
Write-Host "Running python_script1.py..."
python $script1Path

# Run python_script2.py
Write-Host "Running python_script2.py..."
python $script2Path
