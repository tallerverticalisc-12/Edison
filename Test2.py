import cv
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from pytesseract import *

originalPic = cv.LoadImageM("picToAnalyze.jpg") 

resize = cv.CreateMat(originalPic.rows/ 10, originalPic.cols / 10, originalPic.type) 

cv.Resize(originalPic, resize)
th3 = cv2.adaptiveThreshold(originalPic,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)