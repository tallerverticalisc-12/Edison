import pytesseract
from PIL import Image 
print pytesseract.image_to_string(Image.open('Letters.jpg'))
load(Image.open('Letters.jpg'))
