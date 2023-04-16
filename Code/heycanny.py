import cv2
img = cv2.imread(r"lena.png")
lower_threshhold=100
higher_threshhold= 200
canny_img = cv2.Canny(img,lower_threshhold,higher_threshhold)
cv2.imshow('canny image',canny_img)
cv2.waitKey(0)