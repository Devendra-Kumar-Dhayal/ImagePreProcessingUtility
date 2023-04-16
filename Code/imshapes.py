#Version 1.0(Final)
#Importing Packages
from tkinter import Y
import cv2
import numpy as np

# Load image, create mask, and draw white circle on mask
image = cv2.imread(r"BlackAlder.png")
dimensions = image.shape
print(dimensions)

mask = np.zeros(image.shape, dtype=np.uint8)

#Taking Input From The User 
val = input('Enter The Shape (Circle/Rectangle)')

#If The User Wants A Circular Mask
if (val=='Circle'):

 x= input("Enter x coordinate:")   
 y= input("Enter y coordinate:")
 r= input("Enter radius:")

 x=int(x)
 y=int(y)
 r=int(r)


 mask = cv2.circle(mask, (x, y), r, (255,255,255), -1) 

#If The User Wants A Rectangular Mask
elif(val=='Rectangle'):
 x1= input("Enter x coordinate:")   
 y1= input("Enter y coordinate:")    
 x2= input("Enter x coordinate:")   
 y2= input("Enter y coordinate:")

 x1=int(x1)
 y1=int(y1)
 x2=int(x2)
 y2=int(y2)
 
 mask = cv2.rectangle(mask, (x1, y1), (x2, y2), (255, 255, 255), -1)


# Mask input image with binary mask
result = cv2.bitwise_and(image, mask)

# Color background white
result[mask==0] = 255

#Displaying Image
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()