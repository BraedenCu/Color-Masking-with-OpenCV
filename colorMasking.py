import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print('What is the lower bound of the color you would like to mask? Make sure it is in HSV format, for example, if you wan to search for blue type 110,50,50 (with same spacing). Enter each individually, first enter 110 and so on')
color1 = int(input())
color2 = int(input())
color3 = int(input())

print('Upper bound? blue would be 130,255,255')
colorupper1 = int(input())
colorupper2 = int(input())
colorupper3 = int(input())

while(1):

    # GET image from camera
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # range of values (light darkness or lightness of color) for color
    lower_blue = np.array([color1, color2, color3])
    upper_blue = np.array([colorupper1, colorupper2, colorupper3])

    # Setup the mask to only do specified colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Mask the frame (yep)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #show new image
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
