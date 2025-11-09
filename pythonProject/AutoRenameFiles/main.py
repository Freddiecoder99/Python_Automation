import os
from datetime import datetime
from pydoc import text

folder_path = "sample_files"
today = datetime.today().strftime("%Y-%m-%d")

files = os.listdir(folder_path)

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)

    if os.path.isfile(old_path):
        _, ext = os.path.splitext(filename)

        new_filename = f"{today}_{index}-{ext}"
        new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")

print("All files renamed successfully!")