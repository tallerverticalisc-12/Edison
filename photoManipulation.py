from pytesser import *
from PIL import Image
from numpy import *
import cv2

original = cv2.imread('test_imageV2.jpg', 0)
original = cv2.medianBlur(original, 5)

#img2Gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

final = cv2.adaptiveThreshold(original, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#img = Image.open('test_imageV2_gray.jpg')
#img.save('test_imageV2.tiff')
#im = Image.open(img)
#text = image_to_string(im)
#text = image_file_to_string(image_file)
#text = image_file_to_string(image_file, graceful_errors=True)
#print "=====output=======\n", text

cv2.imwrite('test_imageV2.tif', final)
image_file = 'test_imageV2.tif'
#im = Image.open(image_file)
#text = image_to_string(im)
#!text = image_file_to_string(image_file)
#text = image_file_to_string(image_file, graceful_errors=True)
#print "=====output=======\n", text