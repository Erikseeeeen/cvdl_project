from clean_dataset import clean_dataset
from reduce_background_images import reduce_background_images
from xml2yolo import xml_to_yolo
from crop_dataset import crop_norway_dataset
from split_dataset import split_dataset

folders = ['China_Drone', 'China_MotorBike', 'Czech', 'India', 'Japan', 'Norway', 'United_States']
classes = []

print('cleaning dataset')
clean_dataset(folders)
print('removing excess background images')
reduce_background_images(folders, 0.1)
if('Norway' in folders):
    print('cropping norway images')
    crop_norway_dataset()
print('converting xml to yolo')
xml_to_yolo(classes, folders)
print('splitting dataset')
split_dataset(folders)