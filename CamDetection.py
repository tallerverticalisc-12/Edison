import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, img = cap.read()

cv2.imwrite("image_testv2.png", img)

cap.release()