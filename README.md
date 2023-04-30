# cvdl_project

### Contents
- The data directory contains dataset descriptions used by yolov5/yolov8 to find the dataset. In in, the hyps directory contains a description of the hyperparameters used
- The preprocessing directory contains scripts used to pre-process the data. You only need to run main.py.
- The scripts directory contains scripts used to train the models, and perform inference


### Setup
1. Retreive dataset and extract it into a datasets/ directory at https://figshare.com/articles/dataset/RDD2022_-_The_multi-national_Road_Damage_Dataset_released_through_CRDDC_2022/21431547/1
2. Preprocessing: run main.py
3. For training with yolov5, clone https://github.com/ultralytics/yolov5 and put it in the root directory. The command used to train is provided at scripts/yolov5_train.sh
4. For training with yolov8, install the package with pip 'pip install ultralytics'. The command used to train is provided at scripts/yolov8_train.sh