# WE DID IT DURING THE CLASS
import cv2

image_path = '../material/home.jpg'

img = cv2.imread(image_path)

# https://docs.opencv.org/4.9.0/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
cv2.imshow('window',img)

# https://docs.opencv.org/4.9.0/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
cv2.waitKey(0)