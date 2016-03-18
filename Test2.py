import Image
from pytesseract import *
photo = Image.open('phototest.tif')
photo.load()
photo.split()
print image_to_string(Image.open(photo))
#Save
#Save 
#Save
#Save