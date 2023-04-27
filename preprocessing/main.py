from clean_dataset import clean_dataset
from xml2yolo import xml_to_yolo
from crop_dataset import crop_norway_dataset
from split_dataset import split_dataset

folders = ['China_Drone', 'China_MotorBike', 'Czech', 'India', 'Japan', 'Norway', 'United_States']
classes = []

print('cleaning dataset')
clean_dataset(folders)
print('cropping norway images')
crop_norway_dataset()
print('converting xml to yolo')
xml_to_yolo(classes, folders)
print('splitting dataset')
split_dataset(folders)