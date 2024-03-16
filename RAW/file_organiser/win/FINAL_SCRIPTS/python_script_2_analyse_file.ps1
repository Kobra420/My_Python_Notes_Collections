# PowerShell script to run python_script1.py and python_script2.py

# Define the paths to the Python scripts
$script1Path = "path\to\python_script1.py"
$script2Path = "path\to\python_script2.py"

# Run python_script1.py
Write-Host "Running python_script1.py..."
python $script1Path

# Run python_script2.py
Write-Host "Running python_script2.py..."
python $script2Path
