# cvdl_project

### Setup
1. clone yolov5 at https://github.com/ultralytics/yolov5.git and put it in the root directory
2. Retreive dataset and extract it into the yolo/datasets/ directory https://figshare.com/articles/dataset/RDD2022_-_The_multi-national_Road_Damage_Dataset_released_through_CRDDC_2022/21431547/1
3. Preprocessing: run main.py


### Running model


> python train.py --img 640 --batch-size -1 --epochs 200 --name norway_cleaned_reducedbackground --data rdd2022norway.yaml --weights yolov5s.pt

useful options
> --noautoanchor