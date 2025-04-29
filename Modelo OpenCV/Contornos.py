import cv2

imagen = cv2.imread('Bac.jpg')
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