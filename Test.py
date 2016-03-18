from pytesser import *
im = Image.open('Letters.jpg')
text = image_to_string(im)
print text