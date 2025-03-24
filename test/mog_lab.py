import numpy as np
import cv2

MAX_FRAMES = 1000
LEARNING_RATE = -1 # Like alpha of the bg_sub_adaptive_mine.py | 0-1 if I want to be absorbed in the background
N_MIXTURES = 5 # Depends on the number of the colors/objects in the scene
BACKGROUND_RATIO = 0.1 # The ratio of the background to the foreground --> higher value means more background (controllare)
NOISE_SIGMA = 1 # The sigma of the noise
HISTORY = 200 # The number of the frames that the model will keep in memory

cap = cv2.VideoCapture("../material/Video.mp4")

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(HISTORY, N_MIXTURES, BACKGROUND_RATIO,NOISE_SIGMA)

for i in range(MAX_FRAMES):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame, LEARNING_RATE)

    cv2.imshow('Video', frame)
    cv2.imshow('FG Mask - Motion Mask', fgmask)

    if cv2.waitKey(1) == ord('q') or not ret:
        break