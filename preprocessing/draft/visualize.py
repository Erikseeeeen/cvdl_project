import cv2

# Define path to input image and bounding boxes file
img_path = '../datasets/RDD2022/Norway/train/images/Norway_000016.jpg'
bbox_file = '../datasets/RDD2022/Norway/train/labels/Norway_000016.txt'

# Read input image
img = cv2.imread(img_path)# Resize the image
img_width = 2400  # set the desired img_width
img_height = int(img.shape[0] * img_width / img.shape[1])  # calculate the corresponding img_height
img = cv2.resize(img, (img_width, img_height))

# Read bounding boxes from file
with open(bbox_file, 'r') as f:
    bounding_boxes = [line.strip().split() for line in f]

# cv2.namedWindow('Image with bounding boxes', cv2.WINDOW_NORMAL)
# cv2.moveWindow('Image with bounding boxes', 0, 0)  # set the window position to (0, 0)
# cv2.setWindowProperty('Image with bounding boxes', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # set the window to fullscreen
# cv2.setWindowProperty('Image with bounding boxes', cv2.WND_PROP_, cv2.WINDOW_NORMAL)  # set the window type to normal


# Draw bounding boxes on the image
for bbox in bounding_boxes:
    print(img.shape[0])
    # Get box coordinates and label
    class_name, x, y, width, height = bbox
    x, y, width, height = int(float(x)*img_width), int(float(y)*img_height), int(float(width)*img_width), int(float(height)*img_height)
    left = int(x - width / 2)
    top = int(y - height / 2)
    right = int(x + width / 2)
    bottom = int(y + height / 2)
    
    # Draw box and label on the image
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    # cv2.putText(img, class_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the image with bounding boxes
cv2.imshow('Image with bounding boxes', img)
cv2.moveWindow('Image with bounding boxes', 0,0)
cv2.waitKey(0)