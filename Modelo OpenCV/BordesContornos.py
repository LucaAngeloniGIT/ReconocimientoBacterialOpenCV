import cv2
 
img = cv2.imread('Bac.jpg') 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite("A.jpg",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagen = cv2.imread('A.jpg')
img_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
ret, frame = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
contours, hierarchy = cv2.findContours(image=frame, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
ImagenContornos = cv2.drawContours(image=imagen, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('None approximation', ImagenContornos)
cv2.waitKey(0)
cv2.destroyAllWindows()