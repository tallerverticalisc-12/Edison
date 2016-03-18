import cv
import cv2
from PIL import Image
from PIL import ImageFilter
from pytesseract import *

originalPic = cv.LoadImageM("picToAnalyze.jpg") 

resize = cv.CreateMat(originalPic.rows/ 10, originalPic.cols / 10, originalPic.type) 

cv.Resize(originalPic, resize)
cvThreshold(image, binary_image,128,255,CV_THRESH_OTSU)
