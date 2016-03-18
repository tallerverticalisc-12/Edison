import pytesseract as pt
import Image as im
from PIL import Image as PILim



print pt.image_to_string(im.open("Letters.jpg").split())
print pt.image_to_string(PILim.open("Letters.jpg"))