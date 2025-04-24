##### ReconocimientoBacterialOpenCV ##### 
Procesamiento de imagen con OpenCV(python) <====> Analisis bacterial del agua <====> Detectar objetos de un video en movimiento 

						tratamiento de una imagen (para detección de bacterias por su forma/color/comportamiento)

1) Preprocesamiento de imagen

 	-Mejorar contraste (Gris) ===> Resuelto
	-Imagen Binaria (treshold) ==> Resuelto
	-Destacar contornos  =====>  Pendiente

2) Segmentación y detección de contornos

   	Funciones como: SimpleBlobDetector() - findContours() y convexHull()- Sobel().

3) Filtrado de contornos por área y forma
   
   	Eliminar los elementos que no nos son útiles, como contornos muy pequeños, muy  grandes o demasiado geometricos
  
4) Analizar el movimiento en la imagen
5) Extracción de descriptores de forma
   

	Parámetros del contorno:
		-Largo (elongación): distinguir bacilos de cocos.
		-Circularidad: ![image](https://github.com/user-attachments/assets/f74b70f0-9397-4d1e-92f4-80815049c283)
		-Aspect Ratio: ancho / alto 
      		Valor ≈ 1 → forma más bien cuadrada o circular.
      		Valor ≫ 1 → muy alargada (bacilo).
    
    -Momentos de imagen (momentos de HU)
      invariantes a escala y rotación

6) Con los parámetros detectados intentar predecir el tipo de morfología bacteriana.


Los distintos tipos de bacterias a analizar:
![image](https://github.com/user-attachments/assets/a1fda4e6-919b-40c8-bb9e-990d8b97549f)
![image](https://github.com/user-attachments/assets/4399bb73-1eec-4ddf-8f69-ad2cab3c23ff)
