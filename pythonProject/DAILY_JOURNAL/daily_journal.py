import os
from datetime import datetime
import subprocess

journal_folder = "journalEntries"
os.makedirs(journal_folder, exist_ok=True)

mood_options = ["Happy", "Neutral", "Sad", "Excited", "Anxious", "Grateful", "Tired"]
print("Select your mood today:")
for idx, mood in enumerate(mood_options, 1):
    print(f"{idx}. {mood}")

while True:
    try:
        mood_choice = int(input("Enter the number corresponding to your mood: "))
        if 1 <= mood_choice <= len(mood_options):
            selected_mood = mood_options[mood_choice - 1]
            break
        else:
            print("Invalid choice. Please choose a valid number.")
    except ValueError:
        print("Invalid Input. Please enter a number.")

today = datetime.now().strftime("%Y-%m-%d")
filename = f"{today}.txt"
filepath = os.path.join(journal_folder, filename)

template = f""" Date: {today}
   
   Today I'm grateful for:
   1. 
   2. 
   3. 
   
   Todays Goal:
   - 
   - 
   - 
   
   Thoughts and reflections:
   -
   
   What did I learn today?
   - 
   mood: {selected_mood}
"""

with open(filepath, "w") as f:
        f.write(template)

try:
    if os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', filepath])
except Exception as e:
    print(f"Could not open the journal file: {e}")

print(f"journal entry ready: {filepath}")
