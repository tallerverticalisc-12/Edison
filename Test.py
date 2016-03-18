from pytesser import *
im = Image.open('Letters.tif')
text = image_to_string(im)
print text