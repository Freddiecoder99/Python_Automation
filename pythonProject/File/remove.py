from pathlib import Path

file_to_delete = Path("MyFolder/renamed_file.txt")
destination_folder = file_to_delete.parent

if file_to_delete.exists():
    file_to_delete.unlink()

try:
    destination_folder.rmdir()
    print(f"Deleted empty folder: {destination_folder}")
except DSError:
    print(f"Folder {destination_folder} is not empty or cannot be removed")
