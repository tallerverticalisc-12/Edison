import pytesseract
from PIL import image 
Image.load('Letters.jpg')
print pytesseract.image_to_string(Image.open('Letters.jpg'))