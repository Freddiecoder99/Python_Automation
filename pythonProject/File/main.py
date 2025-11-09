import os
import shutil
from pathlib import Path

folder_path =Path("MyFolder")
folder_path.mkdir(exist_ok=True)

file_path = folder_path / "sample.txt"
file_path.write_text("This is a test file")

new_file_path = Path("MyFolder/rename_file.txt")
file_path.replace(new_file_path)

destination_folder = Path("Archive")
destination_folder.mkdir(exist_ok=True)

shutil.move(new_file_path, destination_folder)
