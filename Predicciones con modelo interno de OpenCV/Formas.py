import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('Bac.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 

contornos, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

hull = cv2.convexHull(contornos[1])

epsilon = 0.1*cv2.arcLength(contornos[1],True)
aprrox = cv2.approxPolyDP(contornos[1],epsilon,True)

cv2.putText(img,"Hull",(700,30),cv2.FONT_HERSHEY_PLAIN,2,(200,50,255),4)
cv2.drawContours(img,[hull],-1,(200,50,255),2)
cv2.drawContours(img, hull, -1, (0,0,0),10)

cv2.putText(img,"approx",(100,30), cv2.FONT_HERSHEY_PLAIN,2,(30,150,240))
cv2.drawContours(img,[aprrox],-1,(30,150,240),2)
cv2.drawContours(img, aprrox,-1,(0,0,0),4) 

cv2.imshow('shapes', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
