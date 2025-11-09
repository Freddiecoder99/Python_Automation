from pathlib import Path
import shutil

source_dir = Path("C:/Users/user/Downloads")

if not source_dir.exists():
   print(f"Directory does not exist: {source_dir}")
else:
    for file in source_dir.iterdir():
        if file.suffix == ".jpg":
           photos_folder = source_dir / "Photos"
           photos_folder.mkdir(exist_ok=True)
           shutil.move(str(file), photos_folder)
