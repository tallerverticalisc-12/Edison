import pytesseract as pt
import Image as im
from PIL import Image as PILim

print pt.image_to_string(im.open("test_img.jpg"))
print pt.image_to_string(PILim.open("test_img.jpg"))