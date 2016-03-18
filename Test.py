import Image
from tesseract import *
print image_to_string(Image.open('test.png'))
print image_to_string(Image.open('test-european.jpg'), lang='fra')