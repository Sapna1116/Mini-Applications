import pytesseract as pt
import os
from PIL import Image 

pt.pytesseract.tesseract_cmd = r"D:\Users\Programs\tesseract"

def convertImgToTxt():
    img = Image.open('img.jpg')
    text = pt.image_to_string(img)
    print(text)

convertImgToTxt()