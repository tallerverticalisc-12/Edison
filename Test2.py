import cv2
from PIL import Image
from pytesseract import *

imgToAnalyze = cv2.imread('imgToAnalyze.jpg')
imgGrayScale = cv2.cvtColor(imgToAnalyze, gray, CV_RGB2GRAY)