import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

image = Image.open('phototest.tif')
image.filter(ImageFilter.SHARPEN)
print pytesseract.image_to_string(image)