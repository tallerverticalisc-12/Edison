import pytesseract
from PIL import Image 

imageTest = Image.open('Letters.jpg')
imageTest.load()

print(pytesseract.image_to_string(imageTest))
