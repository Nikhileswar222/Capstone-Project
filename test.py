#!/usr/bin/env python
import numpy as np
import sys
import cv2
import os
import pytesseract
from gtts import gTTS
from PIL import Image
from resizeimage import resizeimage
import time 

cap = cv2.VideoCapture(-1)
sample=0;
error=0
#time.sleep(2)
new_height=0
while(cap.isOpened()):
#while(True):
    ret, img = cap.read()
    if ret:
        error=1
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #adapt1 = cv2.adaptiveThreshold(gray,130,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,153,40)
        cv2.imshow('frame',img)
        #print(adapt1)
        cv2.imwrite('frame.png',img)
        cv2.waitKey(1)
        sample=sample+1
    if (sample == 2):
         sample =0;
        # resized_image=cv2.resize(img,(441,303))
         cv2.imwrite('fra12.png',img)
         #is_valid =resizeimage.resize_cover.validate(img,[200,100])
         #print(is_valid)
         #if is_valid:
         #    cover=resizeimage.resize_cover(img,[200,100])
         #    cover.save('fr.jpeg',image.format)
         break

cap.release()
if error ==0:
    print('Camera is interrupted\nPlease execute the script again')
    cv2.destroyAllWindows()
if error ==1:
   print('image is caputured')
im = Image.open("frame.png")

#text = pytesseract.image_to_boxes(im,lang = 'eng',config = '-psm 7',output_type='Output.STRING' )
#text = pytesseract.image_to_boxes(im,lang = 'eng',config = '-psm 7',nice=0,output_type='string' )
#temp = text.encode('utf-8')
#type(text)
##############espeak#####################
#lag = 'en'
#myobj = gTTS(text=text,lang=lag, slow =False)
#myobj.save("test.mp3")
#os.system("mpg321 test.mp3")
###########################################
#print(text)
cv2.destroyAllWindows()
