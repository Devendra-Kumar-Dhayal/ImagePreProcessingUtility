import cv2
from cv2 import imshow
import numpy as np

#Morph Function
def morph(a):
 img = cv2.imread('a',0)
 kernel = np.ones((5,5),np.uint8)
 gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
 cv2.imshow('Gradient',gradient)
 cv2.waitKey(0)

morph(1)
