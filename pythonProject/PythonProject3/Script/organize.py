import os
import shutil

file_types = {
    'Image': ['.jpg', '.png', '.jpeg'],
    'Documents': ['.pdf', '.docx'],
    'Texts': ['.txt'],
    'Script': ['.py']
}

path = '.'

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext (file)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                break
