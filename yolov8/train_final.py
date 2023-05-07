from comet_ml import Experiment
from ultralytics import YOLO

API_KEY = ''
experiment = Experiment(API_KEY, project_name="yolov5")

# Load a model
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="data/rdd2022.yaml", epochs=300, batch=-1, imgsz=1280, name='final_small_pre',
            hsv_h = 0.015, hsv_s = 0.7, hsv_v = 0.4, degrees = 0.0, translate = 0.1,
            scale = 0.9, shear = 0.0, perspective = 0.0, flipud = 0.0, fliplr = 0.5, mosaic = 1.0,
            mixup = 0.1, copy_paste = 0.1, )



metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
success = model.export(format="onnx")  # export the model to ONNX format

experiment.end()
