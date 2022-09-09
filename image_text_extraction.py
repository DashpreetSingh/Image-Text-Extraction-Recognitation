# -*- coding: utf-8 -*-
"""image text extraction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zd2pXI_iTLzUfjcYxJCdrOWmw8VjB4CH
"""

!pip install easyocr

import easyocr        #easy ocr is used to recogination the image in textual form 
reader = easyocr.Reader(['en','hi'])

import cv2       #its load an image from an specified file
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageFont, ImageDraw, Image     #PIL is python image library its help to save and manuplate the different images



aadhar_front = reader.readtext("/content/drive/MyDrive/data/IMG_20220909_105502.jpg", paragraph=True)

print("aadhar card frontside details :")
aadhar_front

img = cv2.imread("/content/drive/MyDrive/data/IMG_20220909_105502.jpg")
spacer = 100
for detection in aadhar_front: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

aadhar_back = reader.readtext("/content/drive/MyDrive/data/IMG_20220909_105511.jpg", paragraph=True)

print("aadhar card backside details : ")
aadhar_back

img = cv2.imread("/content/drive/MyDrive/data/IMG_20220909_105511.jpg")
spacer = 100
for detection in aadhar_back: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

pan_card = reader.readtext("/content/drive/MyDrive/data/IMG_20220909_105521.jpg", paragraph=True)

print("pancard details :")
pan_card

img = cv2.imread("/content/drive/MyDrive/data/IMG_20220909_105521.jpg")
spacer = 100
for detection in pan_card: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3) #in this line we set the image, starting_point, end_point, and in last we set BGR.
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)  #cv2.putText is used to draw a text string on any image 
    spacer+=15
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
