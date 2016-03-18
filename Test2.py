import cv2
from PIL import Image
from pytesseract import *

imgToAnalyze = cv2.imread('imgToAnalyze.jpg')

imgGrayScale = cv2.cvtColor(imgToAnalyze, cv2.COLOR_BGR2GRAY)
cv2.imwrite('imgGrayScale.jpg', imgGrayScale)

#imgThreshold = cv2.adaptiveThreshold(imgGrayScale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)