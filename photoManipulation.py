import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
tempFrames = 15

for i in range(0, tempFrames):
	ret, img = cap.read()	

if ret:
	cv2.imwrite("imgToAnalyze.jpg", img)

cap.release()

def getImage():
    imgToAnalyze = Image.open('imgToAnalyze.jpg')
    imgToAnalyze.filter(ImageFilter.SHARPEN)
    
    print pytesseract.image_to_string(imgToAnalyze)
    
getImage()
