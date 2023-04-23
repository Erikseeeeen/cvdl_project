import os
import shutil

# specify the source and destination folders
source_folder = "../datasets/RDD2022_released_through_CRDDC2022/RDD2022/Norway/Norway/train/labels"
dest_folder   = "../datasets/RDD2022_released_through_CRDDC2022/RDD2022/Norway/Norway/val/labels"

# get a list of files in the source folder
files = os.listdir(source_folder)

# loop through the first 100 files and move them to the destination folder
for file in files[:1600]:
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        shutil.move(file_path, dest_folder)
        print(f"Moved {file} to {dest_folder}")