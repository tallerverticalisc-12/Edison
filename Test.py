import Image
from pytesseract import image_to_string
print image_to_string(Image.open('phototest.tif'))
#Save