import Image
from tesseract import image_to_string
print image_to_string(Image.open('test.png'))
print image_to_string(Image.open('test-european.jpg'), lang='fra')