import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

#GRAYSCALE
img = cv2.imread('../material/home.jpg', cv2.IMREAD_GRAYSCALE) # Even converting to grayscale, the image is still read as BGR
assert img is not None, "file could not be read, check with os.path.exists()"
cv2.imshow('img',img)
cv2.waitKey(0)

hist = cv2.calcHist([img],[0],None,[256],[0,255])

plt.hist(img.ravel(),256,[0,256]); plt.show()


#RGB
# Load image in color
img = cv2.imread('../material/home.jpg')
assert img is not None, "File could not be read, check with os.path.exists()"

# Split channels
b, g, r = cv2.split(img)

# Compute histograms
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(8, 6))
plt.plot(hist_r, color='red', label='Red Channel')
plt.plot(hist_g, color='green', label='Green Channel')
plt.plot(hist_b, color='blue', label='Blue Channel')
plt.title('RGB Histograms')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#CALCULATE HISTOGRAM FROM A REGION
img = cv2.imread('../material/home.jpg', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()

