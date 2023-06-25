#Libreria Analizador de argumentos
import argparse
import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from joblib import load

warnings.filterwarnings("ignore")

#Objetivo:
# Predicir el cancer de mama a partir de datos medicos 

# ArgumentParse para leer el argumento
ap = argparse.ArgumentParser()

#Añadir parametros
#Permite recibir la ruta del modelo entrenado
ap.add_argument('--modelo', required=True, help='Ruta del archivo del modelo entrenado')

# nargs='+' --> permite recibir multiples valores
ap.add_argument('--datos', nargs='+', type=float, required=True, help='Ingrese los valores de los 30 parametros en una lista')

#Permite obtener el objeto que contiene los valores ingresados
args = ap.parse_args()

# Permite obtener los valores ingresados por el usuario
ruta_modelo = args.modelo
datos = args.datos

# Verificar si se ingreso los 30 valores
if len(datos) != 30:
    print("Error: Se deben ingresar los 30 datos:")
    print("\tradius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean")
    print("\tconcavity_mean, concave, symmetry_mean, fractal_dimension_mean, radius_se, texture_se")
    print("\tperimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_se, symmetry_se")
    print("\tfractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst")
    print("\tcompactness_worst, concavity_worst, concave_worst, symmetry_worst, fractal_dimension_worst")
    exit(1)

# Nombre de las columnas
columnas = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean',
    'concavity_mean', 'concave', 'symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se',
    'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave_se', 'symmetry_se',
    'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

# Crear el DataFrame con los valores ingresados
paciente = pd.DataFrame([datos], columns=columnas)

# Normalización de los datos del paciente
ss = StandardScaler()
pac_norm = ss.fit_transform(paciente)


# PCA
pca = PCA(n_components=1)
pac_pca = pca.fit_transform(pac_norm)


# Cargar el modelo entrenado desde el archivo utilizando joblib
modelo = load(ruta_modelo)

# Realizar la predicción utilizando el modelo cargado
resultado = modelo.predict(pac_pca)

# Imprimir el resultado de la predicción
print("\n\tResultado")
print("\t----------------")
if resultado[0] == 0:
    print("\t\tEl cancer es benigno.")
else:
    print("\t\tEl cancer es maligno.")
print("\t----------------")
