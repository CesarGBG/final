import pandas as pd 

# 1. Cargar el archivo CSV con codificación adecuada
df = pd.read_csv("comentarios_video1.csv")

# 2. Ver primeras filas
print("Primeras filas del archivo:")
print(df.head())

# 3. Ver nombres de columnas
print("\nColumnas disponibles:")
print(df.columns)
