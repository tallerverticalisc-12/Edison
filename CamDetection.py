import numpy as np
import cv2

cap = cv2.VideoCapture(0)
tempFrames = 15

for i in range(0, tempFrames):
	ret, img = cap.read()	

if ret:
	cv2.imwrite("imgToAnalyze.jpg", img)

cap.release()