import os

import cv2

from text_processing.ocrpro import get_ocr

# GEt images
# CAll OCR
# Get Prediction


image_path = "E:/foodpharmer\data\sp1.jpg"

img = cv2.imread(image_path)

if img is None:
    raise ValueError("Error loading the image. Please check the file path.")

find_text = get_ocr()
imtext = find_text.ocr_from_image(img, debug=True)

