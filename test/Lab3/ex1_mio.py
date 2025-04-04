import numpy as np
import cv2


cap = cv2.VideoCapture('../../material/Video2.mp4')
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
         print("Can't receive frame (stream end?). Exiting ...")
         break
    frame_copy = frame.copy() # // FULL COPY
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners = cv2.goodFeaturesToTrack(
        frame_gray, 
        maxCorners=100,
        qualityLevel=0.01,
        minDistance=10,
        blockSize=3,
    )
    
    corners,status,err = cv2.calcOpticalFlowPyrLK(frame_copy,
                                                  frame, 
                                                  corners,
                                                  None)
    
    int_corners = corners.astype(int)
    for i, corner in enumerate(int_corners):
      x, y = corner.ravel()
      color = np.float64([i, 2 * i, 255 - i])
      cv2.circle(frame_copy, (x, y), 3, color)
      cv2.imshow('GFF', frame_copy)

    #cv2.imshow('frame_gray', frame_gray)
    
    corners
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



#int_corners = corners.astype(int)
#for i, corner in enumerate(int_corners):
 #   x, y = corner.ravel()
  #  color = np.float64([i, 2 * i, 255 - i])
   # cv2.circle(frame_copy, (x, y), 3, color)
    #cv2.imshow('GFF', frame_copy)
    