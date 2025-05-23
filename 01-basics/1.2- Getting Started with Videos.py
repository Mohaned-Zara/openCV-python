"""
# what I've learned:
read video, display video, and save video.
capture video from a camera and display it.
these functions : cv.VideoCapture(), cv.VideoWriter()
"""
import numpy as np
import cv2 as cv

# Playing Video from file
""" uncomment :)
cap = cv.VideoCapture('Resources\Videos\dog.mp4')
 
while cap.isOpened():
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
 
    cv.imshow('frame', frame)
    if cv.waitKey(25) == ord('d'): #use appropriate time for cv.waitKey(),  25 milliseconds will be OK in normal cases.
        break
 
cap.release()
cv.destroyAllWindows()
"""

# Capture Video from Camera
#! currently not working 

#Saving a Video
""" uncomment :)

#cv.VideoWriter('o/p_file_name', FourCC_code , fps, Frame_dimensions, isColor_flag)

cap = cv.VideoCapture('Resources\Videos\dog.mp4')
ret, frame = cap.read()

fourcc = cv.VideoWriter_fourcc(*'mp4v') #XVID for windows & linux --> .avi, for mp4 write mp4v
out = cv.VideoWriter('Resources\Videos\dog_test_save.mp4', fourcc  , 20.0, (frame.shape[1],frame.shape[0]),False)

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
        # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    out.write(gray)

    cv.imshow('frame', gray)
    if cv.waitKey(25) == ord('d'): 
        #use appropriate time for cv.waitKey(),25 milliseconds will be OK in normal cases.
        break
    
cap.release()
out.release()
cv.destroyAllWindows()
"""
