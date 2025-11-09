import tkinter as tk
from scheduler import start_schedule


def start():
    status_label.config(text="Scheduler Started!")
    start_schedule(display_area)


root = tk.Tk()
root.title("Message Scheduler GUI")
root.geometry("400x400")
root.resizable(width=False, height=False)

start_button = tk.Button(root, text="Start Scheduling", command=start, font=("Arial", 12))
start_button.pack(pady=10)

status_label = tk.Label(root, text="Scheduler Not Working", font=("Arial", 10))
status_label.pack()

display_area = tk.Text(root, height=15, width=46, font=("Consolas", 10))
display_area.pack(pady=10)

root.mainloop()
