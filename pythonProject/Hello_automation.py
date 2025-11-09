import os
from datetime import datetime

print('Hello Automation! Starting my first automated task....')

folder_name = "pythonProject"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully!")

file_path = os.path.join(folder_name, 'message.txt')
with open(file_path, "w") as file:
    file.write("This file was created by my first Python Automation script!\n")
    file.write(f"Timestamp: {datetime.now()}\n")

print(f"File 'message.txt' created inside '{folder_name}' with a custom message.")