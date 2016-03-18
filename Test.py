from PIL import Image
from pytesser import *

imageTest = Image.open('Letters.jpg')
imageTest.load()

print(pytesseract.image_to_string(imageTest))
