import cv2
import numpy as np

imgToAnalyze = cv2.imread('imgToAnalyze.jpg', 0)
imgToAnalyze = cv2.medianBlur(imgToAnalyze, 5)

imgConverted = cv2.adaptiveThreshold(imgToAnalyze, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imgwrite('imgConverted.jpg', imgConverted)


