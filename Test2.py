import Image
from PIL import *
import pytesseract

image = Image.open('phototest.tif')
image.filter(ImageFilter.SHARPEN)
print pytesseract.image_to_string(image)