import cv2
import numpy as np

img = cv2.imread("")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 11, 2)

ListaContornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for i, contorno in enumerate(ListaContornos):
    area = cv2.contourArea(contorno)
    if area < 100:  # Filtrar contornos de area muy pequeña
        continue

    Perimetro = cv2.arcLength(contorno, True) #True para contorno cerrado
    x, y, ancho, alto = cv2.boundingRect(contorno) #Rectangulo maximo que encierra el contorno
    aspect_ratio = float(ancho) / alto #tiende a 0 La recta vertical, tiende a infinito la recta horizontal
    circularity = 4 * np.pi * area / (Perimetro * Perimetro + 1e-5)  #evitar división por cero

    if circularity > 0.8:
        tipo = "Circular"
        color = (0, 255, 0)
    elif aspect_ratio > 1.5:
        tipo = "AlargadoHorizontal"
        color = (255, 0, 0)
    elif aspect_ratio < 0.5:
        tipo = "AlargadoVertical"
        color = (255, 0, 0)
    else:
        tipo = "Otro"
        color = (0, 0, 255)


    cv2.drawContours(img, [contorno], -1, color, 2)
    cv2.putText(img, str(tipo), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)


cv2.imshow("Clasificacion morfologica", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
