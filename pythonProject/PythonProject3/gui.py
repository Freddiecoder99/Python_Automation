import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

file_types = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Scripts': ['.py', '.js', '.html', '.css']
}


def organize_by_type(folder):
    """Organize files by their file type/extension."""
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            for category, extensions in file_types.items():
                if ext in extensions:
                    folder_path = os.path.join(folder, category)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    break


def organize_by_date(folder):
    """Organize files by their modification date."""
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            folder_path = os.path.join(folder, date_folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))


def start_organizing():
    """Handle the folder selection and organization process."""
    folder = filedialog.askdirectory(title="Select Folder to Organize")

    if not folder:
        return

    try:
        if var.get() == "type":
            organize_by_type(folder)
            messagebox.showinfo("Success", "Files organized by type!")
        else:
            organize_by_date(folder)
            messagebox.showinfo("Success", "Files organized by date!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x250")
root.resizable(False, False)

# Title label
tk.Label(
    root,
    text="Choose how to organize your files:",
    font=('Arial', 14, 'bold')
).pack(pady=20)

# Radio button variable
var = tk.StringVar(value="type")

# Radio buttons frame for better organization
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

tk.Radiobutton(
    radio_frame,
    text="By File Type",
    variable=var,
    value="type",
    font=('Arial', 11)
).pack(anchor='w', padx=20)

tk.Radiobutton(
    radio_frame,
    text="By Date Modified",
    variable=var,
    value="date",
    font=('Arial', 11)
).pack(anchor='w', padx=20)

# Organize button
tk.Button(
    root,
    text="Select Folder & Organize",
    command=start_organizing,
    bg="#4CAF50",
    fg="white",
    font=('Arial', 12, 'bold'),
    padx=20,
    pady=10,
    cursor="hand2"
).pack(pady=20)

root.mainloop()