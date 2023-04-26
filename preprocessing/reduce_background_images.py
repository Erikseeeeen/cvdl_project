from PIL import Image
import os
import xml.etree.ElementTree as ET



def reduce_background_images(folders, goal_background_ratio=0.1):
    
    total_checked_images              = 0
    total_remaining_files             = 0
    total_original_background_images  = 0
    total_remaining_background_images = 0
    for folder in folders:
        current_files_checked               = 0
        current_files_remaining             = 0
        current_original_background_images  = 0
        current_remaining_background_images = 0

        source_image_folder = f'../datasets/RDD2022/{folder}/train/images'
        source_xml_folder = f'../datasets/RDD2022/{folder}/train/annotations/xmls'
        files = os.listdir(source_xml_folder)
        for i, file in enumerate(files):
            current_files_checked+=1
            current_files_remaining+=1

            xml_path = os.path.join(source_xml_folder, file)
            image_path = os.path.join(source_image_folder, file[:-4] + '.jpg')
            if os.path.isfile(xml_path):
                mytree = ET.parse(xml_path)
                myroot = mytree.getroot()
                
                background = True
                for name in myroot.iter('name'):
                    if (name.text != 'rotation'):
                        background = False

                if(background):
                    current_original_background_images  += 1
                    current_remaining_background_images += 1
                    if(current_remaining_background_images / current_files_checked > goal_background_ratio):
                        os.remove(xml_path)
                        os.remove(image_path)
                        current_remaining_background_images -= 1
                        current_files_remaining             -= 1
                        
        print(folder)
        print(f"{current_files_checked=}")
        print(f"{current_files_remaining=}")
        print(f"{current_original_background_images=}")
        print(f"{current_remaining_background_images=}")

        total_checked_images              += current_files_checked
        total_original_background_images  += current_original_background_images
        total_remaining_background_images += current_remaining_background_images
        total_remaining_files             += current_files_remaining

    print(f"{total_checked_images=}")
    print(f"{total_remaining_files=}")
    print(f"{total_original_background_images=}")
    print(f"{total_remaining_background_images=}")

if __name__ == "__main__":
    folders = ['China_Drone']#, 'China_MotorBike', 'Czech', 'India', 'Japan', 'Norway', 'United_States']
    reduce_background_images(folders, 0.1)