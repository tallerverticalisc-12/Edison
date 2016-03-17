import cv2

camera_port = 0
ramp_frames = 30

camera = cv2.VideoCapture(camera_port)

def getImage():
     retval, im = camera.read()
     return im
    
for i in xrange(ramp_frames):
    temp = getImage()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = getImage()
file = "/home/root/Edison/testPic.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
    
    

