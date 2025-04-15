import cv2
import numpy as np

img = cv2.imread("Bac.jpg")

def identify_moles (image):
    keypoints = detector.detect(image)
    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT) 
    return blobs

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 10;
params.maxThreshold = 200;
params.filterByArea = True
params.minArea = 0.1 #1500
params.filterByCircularity = True
params.minCircularity = 0.1 #0.1
params.filterByConvexity = True
params.minConvexity = 0.87 #0.87
params.filterByInertia = True
params.minInertiaRatio = 0.01 #0.01

detector = cv2.SimpleBlobDetector_create(params)

image_with_blobs = identify_moles(img)

cv2.imshow('identified moles', image_with_blobs)    
cv2.waitKey(0)
cv2.destroyAllWindows()