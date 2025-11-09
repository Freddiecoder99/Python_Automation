import os
import shutil

folder_path = r'files'

file_types = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.rar', '.zip']
}

for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder_name, file))
                break

print("File/Folder organized successfully")