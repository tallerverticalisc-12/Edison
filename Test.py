import PIL import Image
from pytesseract import image_to_string

image = Image.open('phototest.tif')

print image_to_string(Image.open(image)
#Save
#Save 