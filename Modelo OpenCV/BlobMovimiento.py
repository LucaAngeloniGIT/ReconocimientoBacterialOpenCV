import cv2
import numpy as np
import time

params = cv2.SimpleBlobDetector_Params()

#params.minThreshold = 10;
#params.maxThreshold = 200;
params.filterByArea = True
params.minArea = 0.1 #1500
params.filterByCircularity = True
params.minCircularity = 0.1 #0.1
params.filterByConvexity = True
params.minConvexity = 0.87 #0.87
params.filterByInertia = True
params.minInertiaRatio = 0.01 #0.01

def reconocerblobs(img):
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(img)
    blank = np.zeros((1,1))
    blobs = cv2.drawKeypoints(img, keypoints, blank, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT) 
    return blobs
cam = cv2.VideoCapture("heliozoo-marino.mp4")

while True:
    ret, img = cam.read()
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_BINARY) ########### MEJOR de todos hasta hora
    frame= cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)

    imagenconblobs = reconocerblobs(frame)

    cv2.imshow('BlobsVideo',imagenconblobs)    
    if (cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()