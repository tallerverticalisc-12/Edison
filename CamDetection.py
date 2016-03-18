import numpy as np
import cv2

cap = cv2.VideoCapture(0)
tempFrames = 30

for i in range(0, tempFrames):
	ret, img = cap.read()	

if ret:
	cv2.imwrite("test_imageV2.png", img)

cap.release()