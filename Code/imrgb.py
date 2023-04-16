#Version 1.1(Final)
#Importing Packages
import cv2
from cv2 import imread
from cv2 import imshow
import numpy



#Creating An Null Function For TrackBar Usage
def empty(a):
  pass

#Importing Image
loc = r"BlackAlder.png"
read = cv2.imread(loc)

#Resizing The Image For A Better Display On The Screen
resize = cv2.resize(read,(400,500))

#Creating TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)

#Giving Range Limit To TrackBars
cv2.createTrackbar("Red Min","TrackBars",0,255,empty)
cv2.createTrackbar("Red Max","TrackBars",255,255,empty)
cv2.createTrackbar("Green Min","TrackBars",0,255,empty)
cv2.createTrackbar("Green Max","TrackBars",255,255,empty)
cv2.createTrackbar("Blue Min","TrackBars",0,255,empty)
cv2.createTrackbar("Blue Max","TrackBars",255,255,empty)

#Creating Masking Parameters
while True:

#Converting The Image To Gray Scale For Better Recognition
 HSV = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
 
 hue_min = cv2.getTrackbarPos("Red Min","TrackBars")
 hue_max = cv2.getTrackbarPos("Red Max","TrackBars")
 sat_min = cv2.getTrackbarPos("Green Min","TrackBars")
 sat_max = cv2.getTrackbarPos("Green Max","TrackBars")
 val_min = cv2.getTrackbarPos("Blue Min","TrackBars")
 val_max = cv2.getTrackbarPos("Blue Max","TrackBars")
 
 #Grouping Min Value Parameters
 lower = numpy.array([hue_min,sat_min,val_min])
 
 #Grouping Max Value Parameters
 upper = numpy.array([hue_max,sat_max,val_max])

 #Masking Out Image Using Above Parameters
 mask = cv2.inRange(HSV,lower,upper)
 MaskResult = cv2.bitwise_and(resize,resize,mask=mask)
 
 #Black And White Mask
 #cv2.imshow('Mask',mask)

 #Exporting Images
 stack = numpy.hstack((MaskResult,resize))
 cv2.imshow('Mask',stack)

 #Time Delay In Which The Code Exits(Miliseconds)
 cv2.waitKey(1)
