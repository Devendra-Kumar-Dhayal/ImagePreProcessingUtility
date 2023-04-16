#Version 1.0(Final)
#Importing Packages
import cv2
from cv2 import imread
from cv2 import imshow
import numpy



#Creating An Null Function For TrackBar Usage
def empty(a):
  pass

def mask(b):

 #Importing Image
 loc = b
 read = cv2.imread(loc)

 #Resizing The Image For A Better Display On The Screen
 resize = cv2.resize(read,(400,500))

 #Creating TrackBars
 cv2.namedWindow("TrackBars")
 cv2.resizeWindow("TrackBars",640,240)

 #Giving Range Limit To TrackBars
 cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
 cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
 cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
 cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
 cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
 cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

 #Creating Masking Parameters
 while True:

 #Converting The Image To Gray Scale For Better Recognition
  HSV = cv2.cvtColor(resize,cv2.COLOR_BGR2HSV)
 
  hue_min = cv2.getTrackbarPos("Hue Min","TrackBars")
  hue_max = cv2.getTrackbarPos("Hue Max","TrackBars")
  sat_min = cv2.getTrackbarPos("Sat Min","TrackBars")
  sat_max = cv2.getTrackbarPos("Sat Max","TrackBars")
  val_min = cv2.getTrackbarPos("Val Min","TrackBars")
  val_max = cv2.getTrackbarPos("Val Max","TrackBars")
 
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


mask(r"BlackAlder.png")
