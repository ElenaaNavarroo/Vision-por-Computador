# Práctica 1

En esta práctica hemos explorado diversos conceptos relacionados con el procesamiento de imágenes utilizando la biblioteca OpenCV en Python. Cada uno de los ejercicios busca aplicar técnicas fundamentales de tratamiento de imágenes y video.

## Contenidos
1. [Tablero de Ajedrez](#1-tablero-de-ajedrez)
2. [Diseño Mondrian](#2-diseño-mondrian)
3. [Modificación de un plano de la imagen](#3-modificación-de-un-plano-de-la-imagen)
4. [Modificación de Canales de Imagen](#4-modificación-de-canales-de-imagen)
5. [Círculos en Píxeles Claros y Oscuros](#5-círculos-en-píxeles-claros-y-oscuros)
6. [Efecto Pop Art](#6-efecto-pop-art)
7. [Conclusión](#7-conclusion)

### 1. Tablero de Ajedrez
En este ejercicio se generó una imagen en blanco y negro que simula un tablero de ajedrez. Para lograr esto, se creó una matriz de 8x8 casillas, donde las casillas alternan entre los colores blanco y negro. El tamaño de cada casilla se ajustó de forma que ocupara 100x100 píxeles, dando como resultado una imagen de 800x800 píxeles en total.

El método utilizado consiste en recorrer cada celda de la matriz y aplicar una condición para determinar si la casilla debe ser blanca o negra, en función de la suma de sus coordenadas. Esto garantiza la clásica alternancia de colores del tablero de ajedrez.

Finalmente, la imagen resultante se visualiza utilizando una herramienta de gráficos que permite mostrar imágenes en escala de grises.

### 2. Diseño Mondrian

En este ejercicio, se creó una imagen inspirada en el estilo de Piet Mondrian. Para ello, se generó una imagen de fondo blanco sobre la cual se añadieron líneas negras que dividen el lienzo en secciones de diferentes tamaños. Dentro de estas secciones, se rellenaron algunos espacios con colores primarios (rojo, amarillo y azul), y en una de las áreas más grandes se utilizó el color gris.

#### Detalles de la imagen:

- **Líneas negras**:
    - Se añadieron líneas verticales y horizontales de grosor constante para dividir el lienzo en secciones. Estas líneas están ubicadas para simular la estética de Mondrian.
  
- **Rectángulos de colores**: 
  - Los rectángulos rojos, amarillos y azules se colocaron en distintas zonas del lienzo, utilizando diferentes tamaños y posiciones para dar un equilibrio visual a la composición.
  - Se utilizó un color gris en una de las áreas más grandes para generar contraste y variedad en la imagen.

El resultado es una composición visualmente equilibrada, que sigue la estética del neoplasticismo característico de Mondrian, con sus líneas gruesas y colores primarios, acompañado de un gris neutro para destacar las áreas coloridas.

La imagen final se muestra sin ejes para enfocarse exclusivamente en el contenido artístico.

### 3. Modificación de un plano de la imagen

En este ejercicio se trabaja con la carga y visualización de imágenes utilizando OpenCV y Matplotlib.

#### Pasos realizados:

1. **Carga de la imagen desde disco**: 
   Se carga una imagen de un archivo utilizando OpenCV. Esto se realiza mediante la función `imread`, la cual carga la imagen en memoria.

2. **Visualización de la imagen original**:
   La imagen cargada inicialmente se muestra utilizando `Matplotlib`. Sin embargo, OpenCV lee las imágenes en formato BGR (azul, verde, rojo), que es diferente del formato RGB estándar (rojo, verde, azul) utilizado por muchas herramientas de visualización.

3. **Conversión de formato BGR a RGB**:
   Para que la imagen se visualice correctamente, se convierte de BGR a RGB utilizando la función `cvtColor` de OpenCV. Después de la conversión, se muestra la imagen ya corregida en formato RGB.

4. **Lectura de la imagen en escala de grises**:
   Finalmente, se vuelve a cargar la imagen, esta vez forzando la lectura en escala de grises, lo que elimina la información de color. La imagen en escala de grises se visualiza utilizando `Matplotlib` con un mapa de colores específico para grises (`gray`).

### 4. Modificación de Canales de Imagen

Este ejercicio utiliza la cámara web para capturar video en tiempo real, separando los canales de color de cada fotograma (rojo, verde y azul). Se realiza una modificación específica en el **canal rojo**, donde se invierte su valor. Posteriormente, los tres canales se concatenan en una sola imagen y se muestran redimensionados en tiempo real.

#### Descripción del proceso:

1. **Captura de video en tiempo real**:
   El código comienza capturando video en vivo desde la cámara web del dispositivo utilizando `cv2.VideoCapture`. En cada iteración del bucle, se procesa un fotograma a la vez.

2. **Separación de los canales de color**:
   Para cada fotograma, se separan los canales de color azul, verde y rojo (BGR), que son las tres componentes principales de la imagen.

3. **Modificación del canal rojo**:
   Una vez separado el canal rojo (R), se invierte su valor. Esto significa que los píxeles con valores bajos (más oscuros) se convierten en valores altos (más claros), y viceversa. Esta operación se realiza restando el valor original de 255, lo que crea un efecto visual llamativo en la imagen final.

4. **Concatenación de los canales**:
   Los tres canales (el canal rojo invertido, el canal verde sin cambios y el canal azul sin cambios) se concatenan horizontalmente en una sola imagen utilizando `np.hstack`. El resultado es una imagen donde se visualizan los tres canales de color de manera conjunta, mostrando claramente cómo la inversión en el canal rojo afecta la composición visual.

5. **Redimensionamiento de la imagen**:
   La imagen concatenada se redimensiona para ajustar el tamaño a la mitad de la altura original y 1.5 veces el ancho original, permitiendo que la imagen resultante se visualice de manera adecuada en la pantalla.

6. **Visualización del video modificado**:
   La imagen redimensionada se muestra en una ventana de video en tiempo real utilizando `cv2.imshow`. El video continúa mostrando los fotogramas modificados hasta que el usuario presiona la tecla `ESC` para finalizar.

7. **Finalización del programa**:
   Una vez que se presiona la tecla `ESC`, el objeto de captura de video se libera y todas las ventanas creadas por OpenCV se cierran.

#### Aplicaciones:
Este tipo de procesamiento es útil para comprender cómo se puede manipular cada canal de color de una imagen de video en tiempo real, creando efectos visuales que pueden tener aplicaciones en áreas como la edición de video, visión por computador o entretenimiento.

### 5. Círculos en Píxeles Claros y Oscuros
Este ejercicio utiliza la cámara web para capturar video en tiempo real y detectar las zonas más claras y más oscuras dentro de cada fotograma. Las zonas más claras se destacan con un círculo rojo, mientras que las más oscuras se destacan con un círculo verde. El procesamiento se realiza en bloques de 8x8 píxeles por cada fotograma capturado.

#### Descripción del proceso:

1. **Captura de video en tiempo real**:
   El código inicia una captura de video desde la cámara web del dispositivo. A través de un bucle continuo, procesa cada fotograma capturado para identificar las zonas con mayor y menor intensidad de luz.

2. **Separación de los canales RGB**:
   Para cada fotograma, se separan los canales de color rojo, verde y azul. Esto permite analizar los valores de intensidad de cada canal por separado.

3. **Procesamiento en bloques 8x8**:
   La imagen se recorre en bloques de 8x8 píxeles. Para cada bloque, se calcula la suma total de los valores RGB de todos los píxeles contenidos en él. Esta suma permite determinar qué bloque es el más claro y cuál es el más oscuro.

4. **Detección de la zona más clara y más oscura**:
   Durante el análisis, el bloque con la suma de valores RGB más alta se considera el más claro y el bloque con la suma más baja se considera el más oscuro. Se registran las coordenadas de estos bloques para marcarlos más adelante.

5. **Dibujo de círculos en las zonas detectadas**:
   - Un **círculo rojo** se dibuja en el centro del bloque más claro.
   - Un **círculo verde** se dibuja en el centro del bloque más oscuro.

6. **Visualización en tiempo real**:
   La imagen modificada, con los círculos dibujados en las zonas más claras y oscuras, se muestra en una ventana en tiempo real.

7. **Salida del programa**:
   El bucle de procesamiento se ejecuta indefinidamente hasta que el usuario presiona la tecla `ESC`, momento en el cual la captura de video se detiene y todas las ventanas se cierran correctamente.

#### Aplicaciones:
Este tipo de procesamiento de video en tiempo real es útil en escenarios donde se necesita analizar la iluminación de una escena, identificar zonas de alta o baja intensidad de luz, o incluso para mejorar la visibilidad de ciertos elementos en aplicaciones de visión por computadora.

### 6. Efecto Pop Art

Este proyecto utiliza la cámara web para capturar video en tiempo real y aplicar diferentes efectos visuales a una imagen dividida en un collage de 9 cuadrantes. Cada cuadrante presenta un efecto único sobre el fotograma capturado, brindando una experiencia visual de estilo "Pop Art". El collage resultante se muestra en tiempo real.

## Descripción del proceso:

1. **Captura de video**:
   El programa comienza capturando video desde la cámara web utilizando OpenCV (`cv2.VideoCapture`). Las dimensiones del video se reducen a un tercio de su tamaño original para facilitar el procesamiento y visualización.

2. **División del collage en 9 cuadrantes**:
   El collage final está compuesto por 9 cuadrantes (3x3), y cada uno de ellos es asignado a una sección específica del fotograma. Los fotogramas se redimensionan para ajustarse a cada cuadrante antes de aplicar los diferentes efectos.

3. **Efectos aplicados en cada cuadrante**:

   - **Primer cuadrante**: Se convierte la imagen en escala de grises, eliminando toda la información de color.
   - **Segundo cuadrante**: Se amplifica el canal azul, mientras que los canales rojo y verde se anulan.
   - **Tercer cuadrante**: Se aplica un efecto de posterización, reduciendo la cantidad de colores mediante una cuantización por bloques.
   - **Cuarto cuadrante**: Se aplica detección de bordes utilizando el algoritmo de Canny, que resalta los contornos de los objetos en el fotograma.
   - **Quinto cuadrante**: Se aplica un filtro de colores tipo sepia, brindando un aspecto cálido y vintage a la imagen.
   - **Sexto cuadrante**: Se aumenta el contraste de la imagen, y además se invierte el canal rojo, creando un efecto visual de alto impacto.
   - **Séptimo cuadrante**: Se aplica un desenfoque gaussiano sobre el fotograma, suavizando los detalles de la imagen.
   - **Octavo cuadrante**: Se convierte la imagen a negativo, invirtiendo los valores de color para lograr un efecto surrealista.
   - **Noveno cuadrante**: Se aplica un efecto de espejo, invirtiendo la imagen horizontalmente.

4. **Visualización en tiempo real**:
   Los fotogramas modificados con estos efectos se combinan en el collage de 3x3 y se muestran en una ventana. El programa continúa procesando los fotogramas hasta que el usuario presiona la tecla `ESC` para finalizar la ejecución.

## Aplicaciones:

Este proyecto puede ser útil en aplicaciones de videoarte, filtros para fotografías, procesamiento de imágenes en tiempo real, entretenimiento interactivo o para aprender y experimentar con diferentes técnicas de manipulación de imágenes en OpenCV. 

## 7. Conclusión

Esta primera práctica ha sido una forma muy divertida y práctica de aprender sobre el procesamiento de imágenes en tiempo real con OpenCV. Al dividir el video en 9 cuadrantes y aplicar diferentes efectos, nosotros pudimos ver cómo pequeños cambios en los canales de color o en la forma en que se procesa cada imagen pueden generar resultados visualmente interesantes y completamente distintos.

En resumen, este proyecto nos permitió no solo aprender nuevas técnicas, sino también poner en práctica formas más divertidas de programar.

