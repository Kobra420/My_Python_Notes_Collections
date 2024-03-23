# PowerShell script to run python_script1.py and python_script2.py

# Define the paths to the Python scripts
$script1Path = "script_path\MOVING_FILE_SCANNING.PY"
$script2Path = "script_path\MOVING_FILE_SCANNING_2.PY"

# Run python_script1.py
Write-Host "Running python_script1.py..."
python $script1Path

# Run python_script2.py
Write-Host "Running python_script2.py..."
python $script2Path
