import subprocess

# Specify the path to the PowerShell executable
powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'

# Specify the path to your PowerShell script
script_path = r'C:\Users\biswa\OneDrive\Documents\GIT\GIT_main\My_Python_Notes_Collections'

# Run the PowerShell script
subprocess.run([powershell_path, '-File', script_path])
