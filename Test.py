import Image
from pytesseract import image_to_string

image = Image.open('phototest.tif')
image.load()
image.split()

print image_to_string(Image.open(image)
#Save
#Save 