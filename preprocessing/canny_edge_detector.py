import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random
img = cv.imread('test_image3.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (1500, 900))
assert img is not None, "file could not be read, check with os.path.exists()"

# edges = cv.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


# convert from rgb to grayscale if needed
if img.ndim == 3:
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur image to remove high frequency noise
blured_img = cv.GaussianBlur(img, (5, 5), 0)

# equalize image
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equilized_img = clahe.apply(blured_img)

# canny edge detection
sigma = 0.33
med_intensity = np.median(equilized_img)
canny_threshold_lower = int(max(0, (1.0 - sigma) * med_intensity))
canny_threshold_upper = int(min(255, (1.0 + sigma) * med_intensity))
edge_img = cv.Canny(
    image=equilized_img,
    threshold1=canny_threshold_lower,
    threshold2=canny_threshold_upper,
    edges=None,
    apertureSize=3,
)