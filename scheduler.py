import subprocess
from datetime import datetime

# Get current time in HHMM format
current_time = datetime.now().strftime("%H%M")

if current_time == "1300":
    subprocess.run(["python", "C:\\path\\to\\first_file.py"])
elif current_time == "1900":
    subprocess.run(["python", "C:\\path\\to\\second_file.py"])
