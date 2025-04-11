# Tracking methods
Region-based tracking -> Set of pixels that share smilar features (color)
Template-based tracking ->use specific models (hands,faces,eyes)
Contour -> Determine position and share of an object over time. useful to track deformable tons
Feature-based tracking -> Select meaningful points (contours, corners)

---

# Feature-based tracking
First select the feature and then determine the displacemente vector

---
## About EX1
cv2.goodFeaturesToTrack
- maxCorners = number of corners that I want to track (features)
- qualityLevel -> is the threshold used for the matrix (a good number is between 0.01 and 0.1)
- minDistance ->
- blockSize -> use numbers between 3/5/7
---

-------
11/04/2025 LAB4

[Kalman Filter Visually Explained](https://www.youtube.com/watch?v=IFeCIbljreY)

Kalman Filter is a template-based tracking because I'm actually modeling stuff here
