# Funciones para ETL
import pandas as pd


#función para cambiar el tipo de formato a fecha con hora
def columna_a_tipo_fecha_hora(df, columna):
   df[columna] = pd.to_datetime(df[columna], format='%Y-%m-%d %H:%M:%S')


#función para cambiar el tipo de formato a entero
def columna_a_tipo_entero(df, columna):
   df[columna] = df[columna].astype(int)


#función para eliminar columnas
def eliminar_columnas(df, lista_columna):
    df.drop(columns=lista_columna, inplace=True)


#funcion para exportar archivos
def exportar_csv(df, url_destino):  
    df.to_csv(url_destino, index=False)

def replazar_datos(lista_o_dato_original, nuevo_dato): 
    df10_sellers['seller_city'].replace(lista_o_dato_original,nuevo_dato,inplace=True)