from PIL import Image
import os
import xml.etree.ElementTree as ET



def clean_dataset(folders):

    dirty_instances = {}

    for folder in folders:
        source_image_folder = f'../datasets/RDD2022/{folder}/train/images'
        source_xml_folder = f'../datasets/RDD2022/{folder}/train/annotations/xmls'
        files = os.listdir(source_xml_folder)

        dirty_instances_current_folder = {}

        for i, file in enumerate(files):
            xml_path = os.path.join(source_xml_folder, file)
            image_path = os.path.join(source_image_folder, file[:-4] + '.jpg')
            if os.path.isfile(xml_path):
                mytree = ET.parse(xml_path)
                myroot = mytree.getroot()
                
                remove_file = False
                for name in myroot.iter('name'):
                    if (name.text != 'D00') and (name.text != 'D10') and (name.text != 'D20') and (name.text != 'D40') and (name.text != 'rotation'):
                        remove_file = True
                        dirty_instances_current_folder[name.text] = dirty_instances_current_folder.get(name.text, 0) + 1

                if(remove_file):
                    os.remove(xml_path)
                    os.remove(image_path)
        print(folder)
        print(f"invalid labels: {dirty_instances_current_folder}")

        for key in dirty_instances_current_folder:
            dirty_instances[key] = dirty_instances.get(key, 0) + dirty_instances_current_folder[key]
    print(dirty_instances)

if __name__ == "__main__":
    folders = ['China_Drone', 'China_MotorBike', 'Czech', 'India', 'Japan', 'Norway', 'United_States']
    clean_dataset(folders)