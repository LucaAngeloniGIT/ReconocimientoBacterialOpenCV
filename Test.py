import cv2
import numpy as np

# Cargar imagen
img = cv2.imread("Bac.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Preprocesamiento
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)

# Detección de contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Clasificación y visualización
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if area < 100:  # Filtrar ruido
        continue

    perimeter = cv2.arcLength(cnt, True)
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = float(w) / h
    circularity = 4 * np.pi * area / (perimeter * perimeter + 1e-5)  # evitar división por cero

    # Clasificación morfológica simple
    if circularity > 0.8:
        tipo = "Coco"
        color = (0, 255, 0)
    elif aspect_ratio > 1.5:
        tipo = "Bacilo"
        color = (255, 0, 0)
    else:
        tipo = "Otro"
        color = (0, 0, 255)

    # Dibujar contorno y etiqueta
    cv2.drawContours(img, [cnt], -1, color, 2)
    cv2.putText(img, tipo, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

# Mostrar resultado
cv2.imshow("Clasificacion morfologica", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
