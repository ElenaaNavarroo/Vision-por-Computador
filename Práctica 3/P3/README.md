# Práctica 3

En esta práctica se abordan varios aspectos relacionados con el procesamiento de imágenes y la clasificación de objetos, utilizando diversas librerías de Python como OpenCV y NumPy. Además, se emplean herramientas de visualización de datos como Matplotlib y Seaborn.

## Autores
[![GitHub María Elena Navarro Santana](https://img.shields.io/badge/GitHub-Elena%20Navarro-red?style=flat&logo=github)](https://github.com/ElenaaNavarroo)
[![GitHub Yeray Álvarez-Buylla Parra](https://img.shields.io/badge/GitHub-Yeray%20Álvarez-blue?style=flat&logo=github)](https://github.com/yabpenserio)

## Tecnologías 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Librerías
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-005F9E?style=flat&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat&logo=seaborn&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

## Objetivos
- Familializarse con OpenCV para el procesamiento de imágenes.
- Aprender a manipular los píxeles de las imágenes correctamente.
- Desarrollar un clasificador de monedas.
- Desarrollar un clasificador de imágenes para microplásticos y evaluarlo.

## Contenidos
1. [Cantidad de monedas](#1-cantidad-de-monedas)
2. [Microplásticos](#2-microplásticos)
3. [Conclusión](#3-conclusión)

### 1. Cantidad de monedas

En esta tarea se carga una imagen de monedas llamada 'monedas.jpg' y se utiliza OpenCV para detectar y dibujar los contornos de las monedas en la imagen. 

![alt text](monedas.jpg)

Luego, se convierte la imagen a escala de grises y aplica un suavizado. 

Con la función `HoughCircles`, se detectan los círculos que representan las monedas. 

Se desplega una ventana emergente y se puede hacer clic en la imagen para seleccionar una moneda de referencia, lo que permite identificar y clasificar las demás monedas en función del radio de esa moneda seleccionada aunque la referencia principal es la de 1 euro. 

![alt text](image.png)

Finalmente, se muestra la imagen procesada, la máscara de dicha imagen y el calculo del valor total de todas las monedas detectadas. Debería sacarse la fotografía paralelo a las monedas para que funcione y ni muy cerca ni muy lejos.

![alt text](image-1.png)

Resultados numéricos:

![alt text](image-6.png)

Se ha intentado clasificar las monedas con el mismo código para la fotografía proporcionada por el profesor y resulta que al no tener la misma escala de fotografía no se detecta correctamente los 2 céntimos.

![alt text](image-5.png)

Resultados numéricos:

![alt text](image-7.png)

Hay que tener en cuenta que el código podría no funcionar con otras imágenes debido a la escala de las mismas. Con lo cual, lo mejor sería probar este clasificador de monedas con una imagen de la misma escala que la primera.

Se ha elaborado otro código para la tarea que detecta mucho mejor las monedas proporcionadas por el profesor, este código define valores de referencia para diámetros y valores monetarios de diferentes monedas, el código permite seleccionar manualmente una moneda aunque la referencia está establecida a 1 euro.

Se carga la imagen, se convierte a escala de grises, y se realiza un umbralizado binario invertido para resaltar las monedas y detectar los contornos.

Se utiliza `cv2.findContours` para identificar los contornos de las monedas en la imagen umbralizada.

Para cada contorno detectado, se calcula el radio del círculo mínimo que lo contiene y se estima el tamaño de cada moneda detectada en función de la referencia seleccionada, comparándolo con los valores de referencia `coin_diameter`. Por otro lado, se determina el valor monetario de cada moneda utilizando `coin_calc` y se suma al valor total de las monedas detectadas.

Por último, se muestra las imágenes con los contornos detectados y la máscara de las monedas resaltadas.

![alt text](image-9.png)

Y se imprime el valor calculado de las monedas detectadas.

![alt text](image-10.png)

Este código tambien tiene el problema de que puede no funcionar correctamente si la imagen de entrada tiene una escala muy diferente a la de la referencia establecida, por lo que se recomienda usar imágenes con escalas similares.

### 2. Microplásticos

En esta tarea, se procesan tres imágenes (fragmentos, pellets y alquitrán) aplicando operaciones de recorte para evitar áreas con sombras, conversión a escala de grises para simplificar el análisis y suavizado de tipo gaussiano para reducir el ruido y suavizar los contornos. 

Fragmentos:
![alt text](fragment-03-olympus-10-01-2020.JPG)

Pellets:
![alt text](pellet-03-olympus-10-01-2020.JPG)

Alquitrán:
![alt text](tar-03-olympus-10-01-2020.JPG)

Para las imágenes de `fragmento` y `pellet`, se utiliza un umbral fijo para binarizar imágenes y para `alquitrán` y se clasifican los contornos detectados según reglas heurísticas para predecir a qué clase pertenece cada objeto.

Se extraen características de cada contorno, como área, perímetro, compacidad, relación de aspecto y el ajuste a una elipse.

![alt text](image-2.png)

![alt text](image-3.png)2

El modelo predice entre estos elementos, y la evaluación del clasificador se realiza mediante una matriz de confusión, y se calculan métricas de `accuracy`, `precision`, `recall` y `f1-score`. 

Finalmente se visualizan los resultados:

![alt text](image-4.png)

Resultados numéricos:

![alt text](image-8.png)

Posibles razones de los resultados obtenidos:

`Accuracy`: La precisión general de la clasificación es del 64%, lo que indica que el modelo acierta en la predicción de la clase en aproximadamente 2 de cada 3 casos.

`Precision`: La precisión de 0.70 refleja que, de las predicciones hechas para cada clase, el 70% fueron correctas. Esto sugiere que el modelo es razonablemente bueno para evitar falsos positivos.

`Recall`: El valor de recall es similar al de accuracy, lo que implica que el modelo detecta correctamente las instancias de cada clase en un 64% de los casos. Es decir, un 36% de los objetos no fueron identificados correctamente.

`F1 Score`: Es la media armónica entre la precisión y el recall, y esta se mantiene en 0.64, lo cual es consistente con los valores de las demás métricas, indicando un balance entre la precisión y la capacidad de detección del modelo.

### 3. Conclusión

En esta práctica, mi compañero y yo hemos implementado con éxito los dos clasificadores requeridos para ambas tareas, lo que nos ha permitido profundizar en las aplicaciones de la visión por computador. A lo largo del proceso, hemos adquirido nuevas habilidades en el uso de herramientas avanzadas de procesamiento de imágenes. Además, la visualización de los resultados ha sido clave para entender mejor el comportamiento del clasificador de microplásticos, lo que nos ha proporcionado una visión más clara sobre su precisión y posibles áreas de mejora.
