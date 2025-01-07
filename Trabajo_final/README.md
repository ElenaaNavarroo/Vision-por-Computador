# Trabajo final: Clasificación y Detección de Imágenes de Hueso

La clasificación y detección de imágenes de huesos es un área de investigación 
crucial en el ámbito médico y científico. Con el creciente volumen de datos en 
radiografías, tomografías y otras imágenes médicas, surge la necesidad de 
herramientas que puedan analizar eficientemente estos datos para asistir en 
diagnósticos precisos. 

## Autores
[![GitHub María Elena Navarro Santana](https://img.shields.io/badge/GitHub-Elena%20Navarro-red?style=flat&logo=github)](https://github.com/ElenaaNavarroo)
[![GitHub Yeray Álvarez-Buylla Parra](https://img.shields.io/badge/GitHub-Yeray%20Álvarez-blue?style=flat&logo=github)](https://github.com/yabpenserio)

## Tecnologías 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Librerías
![Torch](https://img.shields.io/badge/Torch-EE4C2C?style=flat&logo=pytorch&logoColor=white)  
![Torchvision](https://img.shields.io/badge/Torchvision-FF6F00?style=flat&logo=pytorch&logoColor=white)  
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)  
![OS](https://img.shields.io/badge/OS-000000?style=flat&logo=linux&logoColor=white)  
![JSON](https://img.shields.io/badge/JSON-5E60CE?style=flat&logo=json&logoColor=white)  
![TQDM](https://img.shields.io/badge/TQDM-FFD43B?style=flat&logo=python&logoColor=white)  
![Math](https://img.shields.io/badge/Math-4CAF50?style=flat&logo=python&logoColor=white)  
![Torchmetrics](https://img.shields.io/badge/Torchmetrics-2196F3?style=flat&logo=pytorch&logoColor=white)  
![Ultralytics](https://img.shields.io/badge/Ultralytics-FF5722?style=flat&logo=python&logoColor=white)  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)   

## Contenidos
1. [Motivación](#1-motivación)
2. [Objetivo](#2-objetivo)
3. [Metodología](#3-metodología)
4. [Enlaces](#4-enlaces)

### 1. Motivación
El análisis eficiente de radiografías, tomografías y otras imágenes médicas es esencial para reducir la carga de trabajo de los profesionales de la salud y minimizar el error humano. Este proyecto explora el uso de algoritmos avanzados para detectar y clasificar imágenes de huesos, optimizando diagnósticos y estableciendo una base para futuras investigaciones.

### 2. Objetivo
Evaluar y comparar el desempeño de los modelos YOLO y RetinaNet mediante métricas como:
- Precisión
- Recall
- mAP@50
- mAP@50-95

### 3. Metodología
El proyecto se llevó a cabo en las siguientes etapas:
1. **Preparación de datos**: Estandarización y división de datasets.
2. **Entrenamiento**:
   - YOLO: Enfocado en velocidad y precisión general.
   - RetinaNet: Optimización mediante Focal Loss y ajuste fino.
3. **Evaluación y análisis**:
   - Métricas estándar y gráficos comparativos.
   - Análisis de eficiencia computacional y calidad de datos.

### 4. Enlaces

- **Enlace a los datasets utilizados**:
  - [Dataset 1](https://universe.roboflow.com/uet-taxila-2fk6f/bone-fracture-28rd8/dataset/1)
  - [Dataset 2](https://universe.roboflow.com/inteligencia-computacional-e1utb/bone-only-fracture-detection)
  - [Dataset 3](https://universe.roboflow.com/bonez/wrist-junk)

## Conclusiones
El modelo YOLO mostró un desempeño superior en todos los datasets estudiados, mientras que RetinaNet enfrentó desafíos técnicos que limitaron su efectividad. Sin embargo, el trabajo sienta las bases para ampliar el análisis, unificar datasets y explorar nuevos algoritmos.

Se adjunta una memoria y un vídeo para este trabajo que explica detalladamente todo el procedimiento seguido.
