# Práctica 2

En esta práctica hemos explorado diversos conceptos relacionados con el procesamiento de imágenes utilizando la biblioteca OpenCV en Python. Cada uno de los ejercicios busca aplicar técnicas fundamentales de tratamiento de imágenes y video.

## Autores
[![GitHub María Elena Navarro Santana](https://img.shields.io/badge/GitHub-Elena%20Navarro-red?style=flat&logo=github)](https://github.com/ElenaaNavarroo)
[![GitHub Yeray Álvarez-Buylla Parra](https://img.shields.io/badge/GitHub-Yeray%20Álvarez-blue?style=flat&logo=github)](https://github.com/yabpenserio)

## Tecnologías 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Librerías
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-005F9E?style=flat&logo=plotly&logoColor=white)
![Time](https://img.shields.io/badge/Time-FF8800?style=flat)

## Objectivos
- Familializarse con OpenCV.
- Aprender a manipular los píxeles correctamente.
- Aprender a desarrollar un demostrador interactivo.
- Experimentar de forma creativa.

## Contenidos
1. [Cuenta de píxeles blancos por filas](#1-cuenta-de-pixeles-blancos-por-filas)
2. [Imagen de Sobel en 8 bits](#2-imagen-de-sobel-en-8-bits)
3. [Demostrador Interactivo de Procesamiento de Imágenes](#3-demostrador-interactivo-de-procesamiento-de-imágenes)
4. [Reinterpretación del Procesamiento de Imágenes](#4-reinterpretación-del-procesamiento-de-imágenes)
5. [Conclusión](#5-conclusión)
6. [Bibliografía](#6-bibliografía)

### 1. Cuenta de píxeles blancos por filas

En esta tarea, se realiza un análisis del número de píxeles blancos en la imagen 'mandril.jpg' en escala de grises, aplicando la detección de bordes de Canny y la reducción de datos para contar los píxeles blancos por filas.

- En primer lugar, se carga la imagen y se convierte a escala de grises para simplificar los demás procesos.

- En segundo lugar, se aplica el algoritmo de Canny, que identifica los bordes de la imagen. Esto crea una imagen en la que los bordes se representan con píxeles blancos.

- En tercer lugar, se calcula cuál es el valor máximo de bordes en una fila y luego se identifican las filas que tienen al menos el 95% o más de ese valor máximo.

- Por último, se muestra la imagen con los bordes detectados y un gráfico que ilustra cuántos bordes hay en cada fila, donde se han resaltado en rojo las filas que cumplen la condición descrita de que sean filas mayor o igual a 95% de píxeles blancos.

#### Aplicaciones

Dentro del ámbito de visión por computador, este tipo de tarea se puede emplear para áreas de detección de imágenes donde sea importante identificar las regiones donde hayan cambios bruscos de intensidad, por ejemplo en vehículos autónomos o sistemas de asistencia al conductor para detectar los carriles de una carretera.

### 2. Imagen de Sobel en 8 bits

En esta tarea, se aplica un análisis de bordes a la imagen 'mandril.jpg', utilizando la detección de bordes de Sobel, seguido de un umbralizado y la detección de píxeles en filas y columnas de la imagen.

- En primer lugar, se aplica un filtro gaussiano para reducir el ruido de la imagen original y eliminar las altas frecuencias, para poder así detectar los bordes correctamente.

- En segundo lugar, se calculan las derivadas en la dirección horizontal y vertical (Sobel X y Sobel Y) para obtener una representación de los bordes en la imagen. Se combinan los dos resultados para reproducir la imagen del mandril en la que sobresalgan los bordes. La imagen resultante que tiene valores de 64 bits, se convierte a una imagen con formato de 8 bits.

- En tercer lugar, se cuenta el número de píxeles que no son cero (blancos) en cada fila y columna de la imagen, similar al proceso realizado con el operador de Canny.

- En cuarto lugar, se calcula el valor máximo de los conteos de píxeles no nulos tanto en filas como en columnas, y se establece un umbral igual o mayor de 95% de ese valor máximo.

- Por último, se remarcan con lineas horizontales y verticales aquellas filas y columnas que cumplen con la condición descrita anteriormente. 

#### Aplicaciones

Este proceso de detección de bordes utilizando Sobel tiene diversas aplicaciones en el campo de la visión por computadora, por ejemplo en el procesamiento de imágenes médicas, como puede ser una radiografías para identificar posibles anomalías.

### 3. Demostrador Interactivo de Procesamiento de Imágenes

En esta tarea se aplican diferentes efectos a la imagen capturada por la webcam en tiempo real.

Primero, se utiliza OpenCV para iniciar la captura de video desde la cámara conectada al dispositivo. A cada fotograma capturado se le aplica un efecto espejo, invirtiendo la imagen horizontalmente. El sistema alterna automáticamente entre tres modos de efectos, cambiando cada 4 segundos.

- Modo 0: Muestra la imagen original con el efecto espejo aplicado.

![alt text](<Captura de pantalla 2024-10-01 210631.png>)

- Modo 1: Aplica un efecto de posterización usando el algoritmo de K-means clustering, que reduce la cantidad de colores en la imagen a un conjunto limitado de "niveles de color" (clusters). Esto genera una imagen simplificada con una paleta de colores estilizada.

![alt text](<Captura de pantalla 2024-10-01 210623.png>)

- Modo 2: Convierte la imagen en un mapa de calor. La imagen en escala de grises se transforma mediante el colormap "JET" de OpenCV, donde los píxeles oscuros se representan con tonos fríos (azules) y los píxeles brillantes con tonos cálidos (rojos y amarillos), creando un efecto visual llamativo.

![alt text](<Captura de pantalla 2024-10-01 210618.png>)

Para finalizar la visualización de estos efectos, basta con presionar la tecla 'ESC' para detener el proceso.

#### Aplicaciones:

Estos efectos se pueden aplicar en redes sociales, donde los usuarios suelen utilizar filtros para sus fotos, en herramientas de edición de imágenes y videos o inclusos en entornos educativos para que los estudiantes puedan interactuar con técnicas de procesamiento de imágenes en tiempo real.

### 4. Reinterpretación del Procesamiento de Imágenes

En esta tarea, se ha realizado una reinterpretación artística inspirada en los videos My Little Piece of Privacy, Messa di Voce y Virtual Air Guitar, los cuales exploran la interacción entre el cuerpo humano, el movimiento y el espacio digital. Se ha desarrollado un demostrador interactivo que captura el movimiento en tiempo real utilizando la webcam de un ordenador, aplicando técnicas de procesamiento de imágenes centradas en la detección de bordes y la identificación de movimiento.

Primero, el programa comienza capturando video desde la cámara web en tiempo real. Cada fotograma se convierte a escala de grises para simplificar el procesamiento y se le aplica un filtro de suavizado gaussiano para reducir el ruido y mejorar la calidad del fotograma.

Acto seguido, el movimiento se detecta mediante la técnica de diferencia de fotogramas, comparando el fotograma actual con el fotograma anterior. Los cambios entre los dos fotogramas se interpretan como áreas de movimiento. Se aplica un umbral para destacar las regiones con mayor variación en los píxeles, que corresponden a las áreas de mayor actividad. Se utiliza el operador Sobel para detectar los bordes en la imagen. Los bordes representan los cambios más significativos en la intensidad de los píxeles, lo que permite identificar los contornos de los objetos en movimiento. Estos bordes se combinan con las áreas detectadas como en movimiento, creando un efecto visual en el que las zonas de actividad aparecen resaltadas por sus contornos.

Por último, el área de movimiento que se haya detectado se enmarcan en un rectángulo, y se resaltan los contornos. El efecto final es una representación dinámica en la que los movimientos en el que se resaltan los bordes de los objetos en movimiento.

![alt text](<Captura de pantalla 2024-10-01 210815.png>)

#### Aplicaciones:

Este tipo de demostrador puede emplearse en galerías de arte o exposiciones interactivas, donde los movimientos de los visitantes son transformados en imágenes artísticas en tiempo real.

### 5. Conclusión

En esta práctica, se profundizado mejor en el uso de procesamiento de imágenes y video en el ámbito de la visión por computador. A lo largo de las actividades propuestas, se ha ganado bastante experiencia tanto en la manipulación de imágenes (detección de bordes y análisis de píxeles), como en el desarrollo de demostradores con video en tiempo real.

En resumen, el desarrollo de esta práctica ayudará en gran medida a futuras prácticas de la asignatura de Visión por Computador, proporcionándonos las habilidades técnicas necesarias y un enfoque creativo para abordar problemas y encontrar soluciones.

###  6. Bibliografía
1. [Enunciado de la práctica](https://github.com/otsedom/otsedom.github.io/tree/main/VC/P2)
2. [My little piece of Privacy](https://www.niklasroy.com/project/88/my-little-piece-of-privacy)
3. [Messa di voce](https://www.youtube.com/watch?v=GfoqiyB1ndE)
4. [Virtual air guitar](https://www.youtube.com/watch?v=FIAmyoEpV5c)

