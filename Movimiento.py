import cv2
import time

cam = cv2.VideoCapture("heliozoo-marino.mp4")
while True:
    ret, img = cam.read()
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(gris, 90, 255, cv2.THRESH_BINARY)
    
    #blur=cv2.GaussianBlur(gris, (3,3), 0) 
    #img = cv2.Canny(image=blur, threshold1=100, threshold2=200)
    contours, hierarchy = cv2.findContours(image=frame, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    
    cv2.imshow('Bordes', img)
    if (cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
