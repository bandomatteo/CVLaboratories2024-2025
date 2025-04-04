# CONSTAINTS: 
# N = 15
# MAX_FRAMES = 1000/2000
# THRESH = 50
# MAXVAL = 255
# TYPE = CV2.TRESH_BINARY

import cv2
import numpy as np

frames = []
N = 15
MAX_FRAMES = 2000
THRESH = 50
MAXVAL = 255

cap = cv2.VideoCapture("../material/Video.mp4")
    

for t in range(MAX_FRAMES):
    ret, frame = cap.read()

    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) 

    

    frames.append(frame_gray)

    if t >= N:
        diff = cv2.absdiff(frames[t-N], frames[t])
        _, motion_mask = cv2.threshold(diff, THRESH, MAXVAL, cv2.THRESH_BINARY)

        
        cv2.imshow('Frame Diff No Tresh', diff)
        cv2.imshow('Motion Mask', motion_mask)
        
    cv2.imshow('Original Frame', frame_gray)


    #cv2.imshow('Frame Diff', diff)
    

    if cv2.waitKey(1) == ord('q') or not ret:
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()