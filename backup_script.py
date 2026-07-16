import os
import shutil
from datetime import datetime

source_folder = "Notes/internship_tasks/Level_5_Task_3/source_folder"

backup_folder = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

os.makedirs(backup_folder)

for file_name in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(backup_folder, file_name)

    if os.path.isfile(source_path):
        shutil.copy2(source_path, destination_path)

print("Backup completed successfully!")
print("Backup folder created:", backup_folder)