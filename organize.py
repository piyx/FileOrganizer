import os
import sys
import shutil
import argparse
from ext import foldername

FILE_NAME = "organize.py"
EXT_NAME = "ext.py"


def organize_files(path):
    path = path+'\\'
    if not os.path.exists(path):
        print("ERROR! Invalid location")
        return
    files = os.listdir(path)
    extns = set([os.path.splitext(file)[1].strip('.') for file in files])

    # Create Folders
    for ext in extns:
        folder = foldername(ext)
        if folder and not os.path.exists(path+folder):
            os.makedirs(path+folder)

    # Move Files To Folders
    for file in files:
        if file in [FILE_NAME, EXT_NAME]:
            continue
        ext = os.path.splitext(file)[1].strip('.')
        folder = foldername(ext)
        if not folder:
            continue

        src = path+file
        dest = path+folder+'/'+file

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"Moved {file} to {folder}")

    print(f"\nSUCCESS! All files organized in {path}")


try:
    location = sys.argv[1]
    organize_files(location)
except Exception:
    print("USAGE: python organize.py <location>")
