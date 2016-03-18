import pytesseract
import requests
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO


def captureImage():
    cap = cv2.VideoCapture(0)
    tempFrames = 15
    
    for i in range(0, tempFrames):
    	ret, img = cap.read()	

    if ret:
	    cv2.imwrite("imgToAnalyze.png", img)

    cap.release()
    
def convertImage():
    imgToAnalyze = Image.open('imgToAnalyze.png')
    imgGrayScale = cv2.cvtColor(imgToAnalyze, cv2.COLOR_BGR2GRAY)
    imgThreshold = cv2.adaptiveThreshold(imgToAnalyze, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    imgToAnalyze.filter(ImageFilter.SHARPEN)
    
    print pytesseract.image_to_string(imgToAnalyze)
    
captureImage()
convertImage()
