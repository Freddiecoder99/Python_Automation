# Top
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

# bottom
delete_file(destination, filename="renamed_sample1.txt")

create_folder(os.path.join(base_dir, "new_folder"))

delete_folder(os.path.join(base_dir, "new_folder"))
