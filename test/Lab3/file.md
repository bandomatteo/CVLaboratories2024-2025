# Tracking methods
Region-based tracking -> Set of pixels that share smilar features
Template-based tracking ->good for instance tracking bottles (fixed shapes)-> Use specific models
Contour -> Determine position and share of an object over time

---

# Feature-based tracking
First select the feature and then determine the displacemente vector

---
## About EX1
cv2.goodFeaturesToTrack
- maxCorners = number of corners that I want to track (features)
- qualityLevel -> is the threshold used for the matrix (a good number is between 0.01 and 0.1)
- minDistance ->
- blockSize -> use numbers between 3/5/74
---
