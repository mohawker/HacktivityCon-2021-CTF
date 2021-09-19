# Load the library
import cv2
import pytesseract
import requests
import shutil
 
img = cv2.imread('flag.png')
    
# If your image is not already grayscale :
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
txt = pytesseract.image_to_string(thresh,config= '--psm 6')
answer = txt.strip()

print(answer)