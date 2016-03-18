import cv2
from PIL import Image
from pytesseract import *

imgToAnalyze = cv2.imread('imgToAnalyze.jpg')
imgToAnalyze = cv2.medianBlur(imgToAnalyze, 5)
thresh1 = cv2.threshold(imgToAnalyze,127,255,cv2.THRESH_BINARY)