# USIL CAPSTONE 202301 G10
DIAGNÓSTICO DE CÁNCER DE MAMA UTILIZANDO DIFERENTE ALGORITMOS DE ML
### Integrantes
- David, Huanachin Sullca
- Gianmarco, Loyola Alvarado

## Descripción del proyecto 
El proyecto tiene como objetivo principal proponer un método para la predicción temprana del cáncer de mama utilizando modelos de aprendizaje automático. Se pretende identificar qué algoritmo es más efectivo y predictivo en la detección de esta enfermedad. El enfoque se basa en el uso de los siguientes modelos: Random Forest (RF), k-Nearest Neighbors (kNN), Regresión Logística (LR), Árboles de Decisión (DT) y Máquina de Vectores de Soporte (SVM).
Aplicando la técnica de Análisis de Componentes Principales (PCA) para reducir la dimensionalidad del conjunto de datos. El cual, implica eliminar características irrelevantes y obtener una representación más compacta y precisa de los datos.

Finalidad: Generar  un método innovador en términos de precisión para predecir el cáncer de mama utilizando técnicas de aprendizaje automático.

## Método
![image](https://github.com/Gianmarco30/USIL_CAPSTONE202301_G10/assets/51091925/29b14054-8394-48d8-8d07-8015b2c83d4e)

## Actividades desarrolladas
- Carga de la data
- Visualizar la información descriptiva de los datos
- Analizar el número de casos benignos y malignos
- Explorar de los datos
- Eliminación de columnas innecesarias
- Conversion de datos a númericos ("M":1, "B":0)
- Asignamos los datos a "X" e "y"
- Estandarización
- Analisis de componentes principales
- División de datos
- Entrenar el modelo (RF, SVM, LR, KNN, NB y DT)
- Validación cruzada 10 veces
- Predecir con la data de prueba
- Matriz de confución
- Calcular las métricas (Accuracy, Precision, Recall, F1-score)
## Data set 
  La data WBCD se obtuvo de Kaggle 
  https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data 
## Ambiente de desarrollo
- Python 3.11.3
- Jupyter
- Miniconda
## Librerías usadas
- Matplotlib
- Numpy
- Pandas
- Sklearn
- Seaborn
- Tabulate
## Configuración del entorno
Se abre el prototipo.py y en la terminal se crea en el entorno-> conda env create -f ruta_de_entorno.yml
![image](https://github.com/Gianmarco30/USIL_CAPSTONE202301_G10/assets/51091925/7118fbdf-982e-4f1a-9961-f4d5c4d3aadb)
Luego activamos el entorno creado con-> conda activate capstone2
y por ultimo se ingresa la muestra para predecir si es maligo o benigno
![image](https://github.com/Gianmarco30/USIL_CAPSTONE202301_G10/assets/51091925/fe9c3c49-21fa-4a51-b699-dde78a5239f6)

## Enlace del video de configuración
https://youtu.be/kGKWsh8yU6I
## Enlace del video DEMO
https://youtu.be/V9kd3sYR0ow
