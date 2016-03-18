from PIL import *
import pytesseract

image = _get_image('phototest.tif')
image.filter(ImageFilter.SHARPEN)
print pytesseract.image_to_string(image)