import os
import shutil

base_dir = "file_operations"
source = os.path.join(base_dir, "source_folder")
destination = os.path.join(base_dir, "destination_folder")

print("Current working Directory:", os.getcwd())
print("Looking for file at:", os.path.join(source, "sample1.txt"))

# Renaming a File
def rename_file(old_name, new_name):
    old_path = os.path.join(source, old_name)
    new_path = os.path.join(source, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} → {new_path}")
    else:
        print("File not found for renaming.")

# Moving a file
def move_file(filename):
    src_path = os.path.join(source, filename)
    dest_path = os.path.join(destination, filename)
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"Moved: {src_path} → {dest_path}")
    else:
        print("File not found to move.")

# Deleting a file
def delete_file(folder, filename):
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print("File not found to delete")

# Create a folder
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print("Folder already exists")

# Delete a Folder
def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Deleted folder: {path}")
    else:
        print("Folder not found to delete.")

if __name__ == "__main__":
    rename_file(old_name="sample.txt", new_name="renamed_sample1.txt")

    move_file("renamed_sample.txt")

    delete_file(destination, filename="renamed_sample1.txt")

    create_folder(os.path.join(base_dir, "new_folder"))

    delete_folder(os.path.join(base_dir, "new_folder"))
