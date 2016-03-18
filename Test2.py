from PIL import Image
from numpy import *
import cv2
from pytesseract import *

imgToAnalyze = cv2.imread('imgToAnalyze.jpg', 0)
imgToAnalyze = cv2.medianBlur(imgToAnalyze, 5)

#img2Gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

imgThreshold = cv2.adaptiveThreshold(imgToAnalyze, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#img = Image.open('test_imageV2_gray.jpg')
#img.save('test_imageV2.tiff')
#im = Image.open(img)
#text = image_to_string(im)
#text = image_file_to_string(image_file)
#text = image_file_to_string(image_file, graceful_errors=True)
#print "=====output=======\n", text

cv2.imwrite('imgConverted.tif', imgThreshold)
imgFile = 'imgConverted.tif'
imgFinal = Image.open(imgFile).load()
text = image_to_string(imgFinal)
text = image_file_to_string(imgFile)
text = image_file_to_string(imgFile, graceful_errors=True)
print "=====output=======\n", text