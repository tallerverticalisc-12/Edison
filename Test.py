try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract

imageTest = Image.open('Letters.jpg')
imageTest.load()

print(pytesseract.image_to_string(imageTest))
