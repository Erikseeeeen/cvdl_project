import os
import shutil

folders = ['China_Drone', 'China_MotorBike', 'Czech', 'India', 'Japan', 'United_States']


for folder in folders:
    # specify the source and destination folders
    source_folder = f"../datasets/RDD2022_released_through_CRDDC2022/RDD2022/{folder}/{folder}/train/labels"
    dest_folder   = f"../datasets/RDD2022_released_through_CRDDC2022/RDD2022/{folder}/{folder}/val/labels"

    # get a list of files in the source folder
    files = os.listdir(source_folder)

    # loop through the first 100 files and move them to the destination folder
    for file in files[:1600]:
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            shutil.move(file_path, dest_folder)
            print(f"Moved {file} to {dest_folder}")