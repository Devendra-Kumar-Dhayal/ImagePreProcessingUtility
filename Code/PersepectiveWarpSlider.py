#Version 2.0(Final)

#Importing Packages
import numpy as np
import cv2

def empty(a):
 pass

#Input
img = cv2.imread(r"lena.png")
dim = img.shape
print(dim)


#Resizing The Output 
width = dim[1]
height = dim[0] 

#Creating TrackBars
#Creating TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,640)

#Giving Range Limit To TrackBars
cv2.createTrackbar("x1","TrackBars",0,dim[1],empty)
cv2.createTrackbar("y1","TrackBars",0,dim[1],empty)
cv2.createTrackbar("x2","TrackBars",dim[1],dim[1],empty)
cv2.createTrackbar("y2","TrackBars",0,dim[1],empty)
cv2.createTrackbar("x3","TrackBars",dim[1],dim[1],empty)
cv2.createTrackbar("y3","TrackBars",dim[0],dim[0],empty)
cv2.createTrackbar("x4","TrackBars",0,dim[1],empty)
cv2.createTrackbar("y4","TrackBars",dim[0],dim[0],empty)

#Initiating Live Image Perspective Module
while True:
    
    X1=cv2.getTrackbarPos("x1","TrackBars")
    Y1=cv2.getTrackbarPos("y1","TrackBars")
    X2=cv2.getTrackbarPos("x2","TrackBars")
    Y2=cv2.getTrackbarPos("y2","TrackBars")
    X3=cv2.getTrackbarPos("x3","TrackBars")
    Y3=cv2.getTrackbarPos("y3","TrackBars")
    X4=cv2.getTrackbarPos("x4","TrackBars")
    Y4=cv2.getTrackbarPos("y4","TrackBars")


    coord = np.array([X1,Y1,X2,Y2,X3,Y3,X4,Y4])


    #Providing (x,y) Coordinates Through An Array
    input = np.float32([[coord[0],coord[1]], [coord[2],coord[3]], [coord[4],coord[5]], [coord[6],coord[7]]])
    output = np.float32([[0,0], [width-1,0], [width-1,height-1], [0,height-1]])

    #Genrating Matrix Of The Image 
    matrix = cv2.getPerspectiveTransform(input,output)
    
    """
    print(matrix.shape)
    print(matrix)
    """
    
    #Doing Prespective Transformation
    imgOutput = cv2.warpPerspective(img, matrix, (width,height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))

    
    """
    print(imgOutput.shape)
    """
    
    #Displaying The
    cv2.imshow("original",img)
    cv2.imshow("result", imgOutput)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows
cv2.waitKey(0)



