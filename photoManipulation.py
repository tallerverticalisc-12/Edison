import pytesseract
import requests
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

cap = cv2.VideoCapture(0)
tempFrames = 15
for i in range(0, tempFrames):
	ret, img = cap.read()	
if ret:
	cv2.imwrite("imgToAnalyze.jpg", img)
cap.release()

def convertImage():
    imgToAnalyze = Image.open('imgToAnalyze.jpg')
    imgToAnalyze.filter(ImageFilter.SHARPEN)
    
    print pytesseract.image_to_string(imgToAnalyze)
    
convertImage()
