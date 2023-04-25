import os
import shutil

# folders = ['China_Drone', 'China_MotorBike', 'Czech', 'India', 'Japan', 'United_States']
folders = ['Norway_Cropped']


for folder in folders:
    # specify the source and destination folders
    source_folder_images = f"../datasets/RDD2022/{folder}/train/images"
    dest_folder_images   = f"../datasets/RDD2022/{folder}/val/images"
    source_folder_labels = f"../datasets/RDD2022/{folder}/train/labels"
    dest_folder_labels   = f"../datasets/RDD2022/{folder}/val/labels"
    os.makedirs(dest_folder_images)
    os.makedirs(dest_folder_labels)

    # get a list of files in the source folder
    image_files = os.listdir(source_folder_images)

    for file in image_files[:1600]:
        image_file_path = os.path.join(source_folder_images, file)
        if os.path.isfile(image_file_path):
            shutil.move(image_file_path, dest_folder_images)
            print(f"Moved {image_file_path} to {dest_folder_images}")
        
        label_file_path = os.path.join(source_folder_labels, file[:-4] + ".txt")
        if os.path.isfile(label_file_path):
            shutil.move(label_file_path, dest_folder_labels)
            print(f"Moved {label_file_path} to {dest_folder_labels}")