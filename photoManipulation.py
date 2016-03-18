from PIL import Image
from numpy import *
import cv2

original = cv2.imread('test_imageV2.jpg')

img2Gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

cv2.imwrite('test_imageV2_gray.jpg', original)
cv2.Threshold(img2Gray, binary_image,128,255, CV_THRESH_OTSU)

img = Image.open('test_imageV2_gray.jpg')
img.save('test_imageV2.tiff')
im = Image.open(img)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print "=====output=======\n", text

