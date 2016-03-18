try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

img = Image.open('test_imageV2.jpg')
img.load()
i = pytesseract.image_to_string(img)
print i