"""
# what I've learned:
Read an image from file (using cv::imread)
Display an image in an OpenCV window (using cv::imshow)
Write an image to a file (using cv::imwrite)
"""
import cv2 as cv
 
img_BGR = cv.imread("Resources\Photos\park.jpg",cv.IMREAD_COLOR) #MREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
img_original = cv.imread("Resources\Photos\park.jpg",cv.IMREAD_UNCHANGED) #IMREAD_UNCHANGED loads the image as is.
img_Gray = cv.imread("Resources\Photos\park.jpg",cv.IMREAD_GRAYSCALE) #IMREAD_GRAYSCALE loads the image as an intensity one.

cv.imshow("Display_BGR",img_BGR)
cv.imshow("Display_image as is", img_original)
cv.imshow("Display_GrayScale", img_Gray)

cv.waitKey(0)
