# CONSTAINTS: 
# N = 15
# MAX_FRAMES = 1000/2000
# THRESH = 50
# MAXVAL = 255
# TYPE = CV2.TRESH_BINARY

import cv2
import numpy as np

background = None
MAX_FRAMES = 2000
THRESH = 50
MAXVAL = 255

cap = cv2.VideoCapture("../material/Video.mp4")
    

for t in range(MAX_FRAMES):
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 

    if t == 0:
        background = frame_gray
    else:
        # Subtract the background from the frame
        diff = cv2.absdiff(background, frame_gray)
        # Apply a threshold to the difference
        ret, motion_mask = cv2.threshold(diff, THRESH, MAXVAL, cv2.THRESH_BINARY)
        # Show the difference and the motion mask
        cv2.imshow('Background', background)
        cv2.imshow('Motion Mask', motion_mask)
    
    cv2.imshow('Original Frame', frame_gray)
    if cv2.waitKey(1) == ord('q') or not ret:
            break


cap.release()
cv2.destroyAllWindows()