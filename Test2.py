from PIL import *
import pytesseract

image = _get_image('phototest.tif')
image.filter(ImageFilter.SHARPEN)
return pytesseract.image_to_string(image)