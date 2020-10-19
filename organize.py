import os
import shutil
import sys

from ext import foldername

FILE_NAME = "organize.py"
EXT_NAME = "ext.py"


def organize_files(path):
    if not os.path.exists(path):
        print("ERROR! Invalid location")
        return

    files = os.listdir(path)
    extns = {os.path.splitext(file)[1].strip(".") for file in files}

    # Create Folders
    for ext in extns:
        folder = foldername(ext) or ''
        new = os.path.join(path, folder)
        if folder and not os.path.exists(new):
            os.makedirs(new)

    # Move Files To Folders
    for file in files:
        if file in [FILE_NAME, EXT_NAME]:
            continue

        ext = os.path.splitext(file)[1].strip(".")
        folder = foldername(ext)
        if not folder:
            continue

        src = os.path.join(path, file)
        dest = os.path.join(path, folder, file)

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"Moved {file} to {folder}")

    print(f"\nSUCCESS! All files organized in {path}")


if __name__ == "__main__":
    try:
        location = sys.argv[1]
        organize_files(location)
    except Exception as e:
        print(f"Error: {e}")
        print("USAGE: python organize.py <location>")
