# Funciones para ETL
import pandas as pd
import re
from pathlib import Path 
import chardet

#función para abrir achivos como dataframe partiendo de multiples formatos

def apertura_archivos(path):
    path = Path(path)
    with open (path,'rb') as f:
        tipoencoding=chardet.detect(f.read())
        file_type_dict = {
            ".csv": pd.read_csv,
            ".json": pd.read_json,
            ".js": pd.read_json,
            ".txt": pd.read_table,
            ".parquet": pd.read_parquet
        }
        try:
            reading_func = file_type_dict[path.suffix]
        except KeyError:
            raise ValueError(f"File type {path.suffix} not supported")
        else:
            if path.suffix == ".csv":
                df = reading_func(path,encoding='utf-8', sep=',', engine="python",decimal=".")
            elif path.suffix in {".json",".js"}:
                df = reading_func(path, precise_float=True)
            elif path.suffix == ".txt":
                df = reading_func(path, sep="|", decimal=".", engine="python")
            elif path.suffix == ".parquet":
                df = reading_func(path,engine="pyarrow")
            return df


#función para cambiar el tipo de formato a fecha con hora
def columna_a_tipo_fecha_hora(df, columna):
    try:
        df[columna] = pd.to_datetime(df[columna], format='%Y-%m-%d %H:%M:%S')
    except ValueError:
        print(f"Error al convertir la columna {columna} a tipo fecha y hora.")

#función para cambiar el tipo de formato a entero
def columna_a_tipo_entero(df, columna):
    try:
        df[columna] = df[columna].astype(int)
    except ValueError as e:
        print(f"Error al convertir los valores de la columna '{columna}' a tipo entero: {e}")

#función para eliminar columnas
def eliminar_columnas(df, lista_columna):
    try:
        df.drop(columns=lista_columna, inplace=True)
    except ValueError as e:
        print(f"Error al eliminar las columnas, error: {e} ")

#funcion para exportar archivos
def exportar_csv(df, url_destino):  
    try:
        df.to_csv(url_destino, index=False)
    except ValueError as e:
        print(f"Error al eliminar exportar los csv, error:{e}")

#se reemplazan datos de la columna por una lista de datos 
def replazar_datos(df,columna,lista_o_dato_original, nuevo_dato): 
    try:
        df[columna].replace(lista_o_dato_original,nuevo_dato,inplace=True)
    except ValueError as e:
        print(f"Error al reemplazar los datos, error:{e}")

#reemplazo de una faccion del str:
def reemplzar_caracter_x_espacio(df,columna,caracter):
    try:
        df[columna] = df[columna].str.replace(caracter, " ")
    except ValueError as e:
        print(f"Error al reemplzar caracter por espacio, error:{e}")

#con este codigo retiramos cualquier caracter que no sea letras, números o espacios. 
#Colocamos una excepción para los emojis ya que podría ser últiles para analisis de sentimiento de ML, a continuación lista de emojis encontrados en los mensajes: 
def limpieza_texto(df,columna):
    allowed_chars = ['💟','😉','😭','💖','💝','🌟','😎','💋','💚','💯','🌷','😠','😡','😃','😊','😱','🐕','😏','😍','🍀','🤔','😀','😘','😢','🤗','😒','😂','😣','🙏🏻','👌','👍🏼','?','👏','🤙🏼','🙌🏻','😀','😆','🔝','🤔','😊','😁','😊','😩','🎁','😟','👎','🏇','👧','💅']
    try:
        df[columna] =  df[columna].apply(lambda x: x if (isinstance(x, str) and any(c in allowed_chars for c in x)) else re.sub(r"[^\w\s]", "", x) if isinstance(x, str) else x)
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')

#eliminamos los espacios vacíos delante y al final del texto
def limpieza_espacios(df,columna):
    try:
        df[columna] = df[columna].str.strip()
    except AttributeError:
        print(f"Error al limpiar espacios en la columna {columna}.")

#esta funcion elimina números al inicio de una cadena de str:
def eliminando_numeros_de_str(df,columna):
    try:
        df[columna] = df[columna].str.replace("^[0-9]+", "", regex=True)
    except AttributeError:
        print(f"Error al eliminar números en la columna {columna}.")

#funcion que reemplaza, lista de signos por nada: 
def elimina_lista_simbolos(df,columna,lista_signos):
    try:
        for i in lista_signos: 
            df[columna] = df[columna].replace(i, "")
    except:
        print("Error al eliminar símbolos de la columna".format(columna))

#funcion que reempla celdas vacías por NaN
def reemplaza_vacios_x_nan(df, columna):
    try:
        df[columna] =df[columna].replace("",'nan')
    except:
        print("Error al reemplazar valores vacíos con NaN en la columna: ", columna)

#funcion que modifica el texto para que esté en formato título
def str_a_titulo(df,columna):
    try:
        df[columna] = df[columna].str.title()
    except (AttributeError, TypeError):
        if TypeError:
            print("Error al transformar los datos en title, revisar el formato de la columna")
        else:
            print('AttributeError') 