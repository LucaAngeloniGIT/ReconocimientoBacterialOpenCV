import cv2
import time

cam = cv2.VideoCapture("heliozoo-marino.mp4")
while True:
    ret, img = cam.read()
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #ret,frame = cv2.threshold(gris, 127,255,0)
    ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_BINARY) ########### MEJOR de todos hasta hora
    #ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_BINARY_INV)
    #ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_TOZERO)
    #ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_TOZERO_INV)

    ############ret,frame = cv2.threshold(gris,127,255,cv2.THRESH_TRUNC)
    #frame = cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,2)
    frame= cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)
    


    img2, contornos= cv2.findContours(image=frame, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image=img, contours=img2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    
    #blur=cv2.GaussianBlur(frame, (3,3), 0) 
    #frame = cv2.Canny(image=blur, threshold1=100, threshold2=200)

    cv2.imshow('Bordes', img)
    if (cv2.waitKey(1) == ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
