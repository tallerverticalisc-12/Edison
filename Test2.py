import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
from StringIO import StringIO

image = _get_image('phototest.tif')
image.filter(ImageFilter.SHARPEN)
print pytesseract.image_to_string(image)

def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))