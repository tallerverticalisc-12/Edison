import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

def getImage():
    image = Image.open('picToAnalyze.jpg')
    image.filter(ImageFilter.SHARPEN)
    
    print pytesseract.image_to_string(image)
    
getImage()
