from PIL import Image
import pytesseract 
import os
import sys
import base64
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
bs64_image = sys.argv[1]

with open("imageToSave.png", "wb") as fh:
    fh.write(base64.decodebytes(bs64_image))

def upload(file):
    text=pytesseract.image_to_string(Image.open(file))
    return text

