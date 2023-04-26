from PIL import Image
import os
import xml.etree.ElementTree as ET

def crop_norway_dataset():
    def clamp(num, min_value, max_value):
        return max(min(num, max_value), min_value)

    source_image_folder = '../datasets/RDD2022/Norway/train/images'
    source_xml_folder = '../datasets/RDD2022/Norway/train/annotations/xmls'

    dest_image_folder = '../datasets/RDD2022/Norway_Cropped/train/images'
    dest_xml_folder = '../datasets/RDD2022/Norway_Cropped/train/annotations/xmls'

    try:
        os.makedirs(dest_image_folder)
    except:
        pass

    try:
        os.makedirs(dest_xml_folder)
    except:
        pass


    files = os.listdir(source_image_folder)

    for i, file in enumerate(files):
        if(i % 1000 == 0):
            print(i)
        image_path = os.path.join(source_image_folder, file)
        if os.path.isfile(image_path):
            img = Image.open(image_path)

            new_height = int(img.height*0.5)
            new_width = int(img.width*0.6)
            box = (0, new_height, new_width, img.height)
            img2 = img.crop(box)
            img2.save(os.path.join(dest_image_folder, file))



            xml_path = os.path.join(source_xml_folder, file[:-4] + '.xml')
            if os.path.isfile(xml_path):
                mytree = ET.parse(xml_path)
                myroot = mytree.getroot()
                
                for ymin in myroot.iter('ymin'):
                    new_ymin = float(ymin.text)-float(new_height)
                    ymin.text = str(clamp(new_ymin, 0, new_height))

                for ymax in myroot.iter('ymax'):
                    new_ymax = float(ymax.text)-float(new_height)
                    ymax.text = str(clamp(new_ymax, 0, new_height))
                

                for xmin in myroot.iter('xmin'):
                    xmin.text = str(clamp(float(xmin.text), 0, new_width))

                for xmax in myroot.iter('xmax'):
                    xmax.text = str(clamp(float(xmax.text), 0, new_width))


                for height in myroot.iter('height'):
                    height.text = str(int(float(height.text)*0.5))

                for width in myroot.iter('width'):
                    width.text = str(int(float(width.text)*0.6))

                    
                mytree.write(os.path.join(dest_xml_folder, file[:-4] + '.xml'))


if __name__ == "__main__":
    crop_norway_dataset()

