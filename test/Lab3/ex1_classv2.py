import cv2
import numpy as np

MAX_CORNERS = 100
QUALITY = 0.01
MIN_DISTANCE = 10 # Minimum distance 2 points
BLOCK_SIZE = 3

cap = cv2.VideoCapture('../../material/Video2.mp4')

frame_counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    
    frame_copy = frame.copy() #  FULL COPY , where I want to print the points
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if frame_counter % 100 == 0:
    # Select GFF Features
        corners = cv2.goodFeaturesToTrack(
            frame_gray, 
            maxCorners=MAX_CORNERS,
            qualityLevel=QUALITY,
            minDistance = MIN_DISTANCE,
            blockSize =BLOCK_SIZE
    )
    else:
        # Optical flow
        corners, status, err = cv2.calcOpticalFlowPyrLK(prev_frame, frame, prev_corners, None)
        
    # Copy the values
    prev_frame = frame.copy()
    prev_corners = corners
    
    # Plot corners
    int_corners = corners.astype(int)
    for i, corner in enumerate(int_corners):
        x, y = corner.ravel()
        color = np.float64([i, 2 * i, 255 - i])
        cv2.circle(frame_copy, (x, y), 3, color)
        cv2.imshow('GFF', frame_copy)
    
    cv2.imshow('GFF', frame_copy)
    cv2.waitKey(1)
    
    frame_counter += 1

cap.release()
cv2.destroyAllWindows()
