import pytesseract
from PIL import image *
print pytesseract.image_to_string(Image.open('Letters.jpg'))