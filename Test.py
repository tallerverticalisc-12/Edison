import pytesseract
from PIL import Image 
Image.load('Letters.jpg')
print pytesseract.image_to_string(Image.open('Letters.jpg'))
