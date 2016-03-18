import cv2
from PIL import Image
from pytesser import *

original = cv2.cv.LoadImage("test_imageV2.jpg")

img2Gray = cv2.CvtColor(original,gray,CV_RGB2GRAY)

cv2.cv.Threshold(img2Gray, binary_image,128,255, CV_THRESH_OTSU)

img = Image.open('test_imageV2.jpg')
img.save('test_imageV2.tiff')
im = Image.open(img)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print "=====output=======\n", text