import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, img = cap.read()

cv2.imwrite("test_imageV2.png", img)

cap.release()