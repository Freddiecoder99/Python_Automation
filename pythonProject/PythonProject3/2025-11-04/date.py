import os
import shutil
from datetime import datetime

path = '.'

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        nod_time = os.path.getmtime(file_path)
        date_folder = datetime.fromtimestamp(nod_time).strftime('%Y-%m-%d')
        folder_path = os.path.join(path, date_folder)
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(file_path, os.path.join(folder_path, file))