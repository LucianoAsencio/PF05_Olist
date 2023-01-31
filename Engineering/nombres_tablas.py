import os

# Esta porción de código se corre una única vez

nombre_tablas = []
ruta_datasets = 'C:/Users/AMD/Desktop/datasets_limpios'

# Este bucle acomoda los nombres de los archivos a la lógica que siguen los nombres de las tablas

for archivo in os.listdir(ruta_datasets):
    archivo = archivo.replace('_',' ')
    archivo = archivo.replace('.csv','')
    archivo = archivo.replace('olist','')
    archivo = archivo.replace('dataset','')
    archivo = archivo.strip()
    archivo = archivo.replace(' ','_')
    archivo = archivo[3:]
    nombre_tablas.append(archivo)


# Se crea el archivo con el nombre de las tablas para la primera carga

tablas = open('C:/Users/AMD/Desktop/registros/nombre_tablas.txt', 'w')
for linea in nombre_tablas:
    tablas.write(f"{linea}\n")

tablas.close()