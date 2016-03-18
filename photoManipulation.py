#photoManipulation.py
#Copyright (C) 2016  Smart Parking

#TThis program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    ##This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
    imgToAnalyze = cv2.imread('imgToAnalyze.png', 0)
    imgThreshold = cv2.adaptiveThreshold(imgToAnalyze, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    imgToAnalyze.filter(ImageFilter.SHARPEN)
    
    print pytesseract.image_to_string(imgToAnalyze)
    
captureImage()
convertImage()
