from PIL import Image
from pytesseract import image_to_string

def read(path_to_image="/home/pi/third-eye/temp/image.jpg"):
    return image_to_string(Image.open(path_to_image))
