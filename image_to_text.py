# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:28:44 2021

@author: samya
"""

from PIL import Image
import pytesseract 
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def upload(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text

print(upload('cover letter.png'))