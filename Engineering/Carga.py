# Este código se correrá cada vez que haya que ingestar nuevos datos en la DB

import pandas as pd
from sqlalchemy import create_engine
import os
import datetime

# Se esconden las credenciales de la DB
archivo_credenciales = open('C:/Users/AMD/Desktop/registros/credenciales.txt', 'r')
lista_credenciales = archivo_credenciales.readlines()


lista_credenciales_aux = []

for n in lista_credenciales:
    n = n.replace("\n","")
    lista_credenciales_aux.append(n)

user = lista_credenciales_aux[0]
password = lista_credenciales_aux[1]
hostname = lista_credenciales_aux[2]
port = lista_credenciales_aux[3]


# Conexión a la base de datos
engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (user, password, hostname, port, "olist_pf"))

# Guardamos variables y leemos los nombres de las tablas
tablas = open('C:/Users/AMD/Desktop/registros/nombre_tablas.txt', 'r')
registro_de_datos = open('C:/Users/AMD/Desktop/registros/registro_de_datos.txt', 'a')
ruta_datasets = 'C:/Users/AMD/Desktop/datasets_limpios'
nombre_tablas = tablas.readlines()
tablas.close()

lista_nombre_tablas = []
contador = 1
datasets = os.listdir(ruta_datasets)

# Se guardan los nombres de las tablas en una lista
for tabla in nombre_tablas:
    tabla = tabla.replace('\n','')
    lista_nombre_tablas.append(tabla)


# Se cambia el formato del nombre del archivo para que coincida con los nombres de las tablas
# y se pueda hacer la comprobación para enviarlo a su tabla correspondiente

for archivo in datasets:
    archivo = archivo.replace('_',' ')
    archivo = archivo.replace('.csv','')
    archivo = archivo.replace('olist','')
    archivo = archivo.replace('dataset','')
    archivo = archivo.strip()
    archivo = archivo.replace(' ','_')
    archivo = archivo[3:]

    # Si el nombre del archivo está en la lista de las tablas
    # lo insertamos en su correspondiente tabla

    if archivo in lista_nombre_tablas:

        # Leemos el archivo
        if contador < 10:
            df = pd.read_csv(ruta_datasets + '/olist_0' + str(contador) + '_' + archivo + '_dataset.csv')
        else:
            df = pd.read_csv(ruta_datasets + '/olist_' + str(contador) + '_' + archivo + '_dataset.csv')

        

        # Escribimos el archivo en la nueva tabla

        # NOTA: En este punto archivo y el nombre de la tabla coinciden
        # por lo que se lo pasa en el parámetro que define en qué tabla se agregarán los datos

        df.to_sql(archivo, engine, if_exists='append', index=False)

        # Escribimos en el registro de datos a qué hora se agregó qué archivo

        if contador < 10:
            registro_de_datos.write('El archivo olist_0' + f'{contador}_' + archivo + '_dataset.csv' + f' se ingestó en la fecha: {datetime.datetime.now()}\n')
        else:
            registro_de_datos.write('El archivo olist_' + f'{contador}_' + archivo + '_dataset.csv' + f' se ingestó en la fecha: {datetime.datetime.now()}\n')

        contador += 1

# Una vez finalizamos de ingestar todos los datos cerramos el archivo de registro
registro_de_datos.close()




