## ETL
'''
Como conclusión del EDA, las modificaciones a realizar para obtener datos limpios para el Data Warehouse son: 

### 1_closed_deals:

 - 'won_date' _ cambio de formato a fecha hora

 Se eliminan las columnas por falta de datos suficientes (NaN o 0): 

 - 'has_gtin' 
 - 'has_company' 
 - 'average_stock' 
 - 'declared_product_catalog_size'
 - 'declared_monthly_revenue'

Se crea un nuevo id en una nueva columna que se coloca al inicio de la tabla.

 - 'closed_deals_id'

### 2_customers: 

Se elimina la columna de customer_unique_id porque no es un id único:

 -  'customer_unique_id'

### 3_geolocation:

Es una table incompleta a pesar de su dimensión ya que no tiene todos los zip_code (códigos postales) presentes en las tablas de Customers y Sellers por lo tanto será eliminada del modelo y se evaluará hacer una nueva tabla de geolocation sin latitud ni longitud, según su posible utilidad. 


### 4_marketing_q_leads:

Se pasan la siguiente columna a formato fecha hora:

 - 'first_contact_date'

### 5_order_items:

Se pasan la siguiente columna a formato fecha hora:

 - 'shipping_limit_date'

Se reemplazan 4 fechas que estan situadas en 2020, reemplazando los valores según el ID de orden de la tabla order por la fecha correcta

### 6_order_payments:

Se cambia de formato a entero: 

 - 'payment_installments'

### 7_order_reviews:

Se pasan las siguientes columnas a formato fecha hora:
 - 'review_creation_date'
 - 'review_answer_timestamp'

Se limpian las columnas del texto title y comments de reviews
 - 'review_comment_title'
 - 'review_comment_message'

### 8_orders:

Se pasan las siguientes columnas a formato fecha hora: 

 - 'order_purchase_timestamp'
 - 'order_approved_at'
 - 'order_delivered_carrier_date'
 - 'order_delivered_customer_date'
 - 'order_estimated_delivery_date'

### 9_product:

Se quitaron los guiones bajos y se reemplazar por espacios: 

 - 'product_category_name'
 
### 10_sellers:

Se agrega normalizan los datos de la columa:

 - 'seller_city'


### 11_category_name:

Se quitaron los guiones bajos y se reemplazar por espacios: 

 - 'product_category_name'
 - 'product_category_name_english'


'''

#_____________________________________________________________

#Importamos las librerias y funciones: 

import pandas as pd
import secrets
from funciones_ETL import *

# Abrimos los datasets en dataframe de pandas 1 por tabla
''''
df1_closed_deals= apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_closed_deals_dataset.csv')
df2_customers=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_customers_dataset.csv')
df3_marketing_qualified_leads=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_marketing_qualified_leads_dataset.csv')
df4_order_items=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_order_items_dataset.csv')
df5_order_payments=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_order_payments_dataset.csv')
df6_order_reviews=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_order_reviews_dataset.csv')
df7_orders=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_orders_dataset.csv')
df8_products=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_products_dataset.csv')
df9_sellers=apertura_archivos('C:/Users/AMD/Desktop/datasets/olist_sellers_dataset.csv')
df10_category_name=apertura_archivos('C:/Users/AMD/Desktop/datasets/product_category_name_translation.csv')
'''

df1_closed_deals= pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_closed_deals_dataset.csv')
df2_customers=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_customers_dataset.csv')
df3_marketing_qualified_leads=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_marketing_qualified_leads_dataset.csv')
df4_order_items=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_order_items_dataset.csv')
df5_order_payments=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_order_payments_dataset.csv')
df6_order_reviews=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_order_reviews_dataset.csv')
df7_orders=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_orders_dataset.csv')
df8_products=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_products_dataset.csv')
df9_sellers=pd.read_csv('C:/Users/AMD/Desktop/datasets/olist_sellers_dataset.csv')
df10_category_name=pd.read_csv('C:/Users/AMD/Desktop/datasets/product_category_name_translation.csv')

#note: la tablas df4_marketing_qualified_leads , es la misma que en EDA se llamaba df4_q_leads (se cambió el nombre para mejor entendimiento del contenido por parte de todo el equipo)

# LIMPIEZA DE DATOS 
# 1_closed_deals:

# Cambio de formato a fecha hora 
columna_a_tipo_fecha_hora(df1_closed_deals,'won_date')

# Eliminando columnas porque poseen en su mayoría valores nulos o ceros
eliminar_columnas(df1_closed_deals,['has_gtin','has_company','average_stock','declared_product_catalog_size','declared_monthly_revenue'])

# Se crea un id de esta tabla
lista_id = []
for i in range(0, len(df1_closed_deals)):
    lista_id.append(secrets.token_hex(16))

df1_closed_deals['closed_deals_id'] = lista_id

# Se extraen en otra tabla 462 datos que corresponden a Sellers que no tienen ordenes asociadas 
# (la tabla se reserva si se requiere la información a futuro)
'''
Dado que se analizaron los datos y se contraron 380 sellers que 
se encuentran en ID seller con cuentas activas 
(ordenes asociadas) y hay 462 ID que corresponden a las ultimas 
fechas, sin ordenes asociadas, esta información se extrae de 
la tabla y se reserva en un dataframe aparte 
'''
lista_ids = df9_sellers['seller_id'].unique()

#datos reservados en la tabla df_aux: 
df_aux = df1_closed_deals[~df1_closed_deals['seller_id'].isin(lista_ids)]

#modificación sobre la tabla original, extrayendo los datos por mascara
df1_closed_deals = df1_closed_deals[df1_closed_deals['seller_id'].isin(lista_ids)]

# Se ordenan las columnas para dejar al id de columna primero
df1_closed_deals = df1_closed_deals.reindex(columns=['closed_deals_id','mql_id', 'seller_id', 'sdr_id', 'sr_id', 'won_date','business_segment', 'lead_type', 'lead_behaviour_profile','business_type'])


# 2_Customers:

# Se elimina la columna de customer_unique_id porque no es un id único
df2_customers = df2_customers.drop(columns='customer_unique_id')
df2_customers['customer_city']=df2_customers['customer_city'].replace("arraial d'ajuda","arraial d ajuda")


# 3 _marketing_quality_leads:

# Cambio de formato a fecha hora (se conserva el tema del formato con hora para homogeinizar en el schema de interelación con el calendar)
columna_a_tipo_fecha_hora(df3_marketing_qualified_leads,'first_contact_date')


# 4_order_items:

# Pasamos a formato la fecha con hora
columna_a_tipo_fecha_hora(df4_order_items,'shipping_limit_date')

#reemplazamos valores únicos que tienen error, la información de base la tomamos segun order ID de la tabla orders
df4_order_items.loc[df4_order_items["shipping_limit_date"] == "2020-04-09 22:35:08", "shipping_limit_date"] = "2017-06-09 13:35:54"
df4_order_items.loc[df4_order_items["shipping_limit_date"] == "2020-02-05 03:30:51", "shipping_limit_date"] = 'nan'
df4_order_items.loc[df4_order_items["shipping_limit_date"] == "2020-02-03 20:23:22", "shipping_limit_date"] ="2017-08-04 00:00:00"


# 5_order_payments:

# Cambio de tipo de dato a entero
columna_a_tipo_entero(df5_order_payments,'payment_installments')


# df6_order_reviews:

# Cambiamos a formato fecha la columna  review_creation_date
columna_a_tipo_fecha_hora(df6_order_reviews,'review_creation_date')
columna_a_tipo_fecha_hora(df6_order_reviews,'review_answer_timestamp')

#limpieza de columnas review_comment_title  y  review_comment_message: 


# Con este codigo retiramos cualquier caracter que no sea letras, números o espacios. 
# Colocamos una excepción para los emojis ya que podría ser últiles para analisis de sentimiento de ML, a continuación lista de emojis encontrados en los mensajes: 
limpieza_texto(df6_order_reviews,'review_comment_title')
limpieza_texto(df6_order_reviews,'review_comment_message')

# Eliminamos los espacios vacíos delante y al final del texto
limpieza_espacios(df6_order_reviews,'review_comment_title')
limpieza_espacios(df6_order_reviews,'review_comment_message')

# Se ha observado que hay muchas líneas que comienzan con números, e inclusive otras que solo poseen números: 
eliminando_numeros_de_str(df6_order_reviews,'review_comment_title')
eliminando_numeros_de_str(df6_order_reviews,'review_comment_message')

# Eliminamos una lista particular de simbolos: 
lista_signos=['?','?!?','??','???','????????']
elimina_lista_simbolos(df6_order_reviews,'review_comment_title',lista_signos)
elimina_lista_simbolos(df6_order_reviews,'review_comment_message',lista_signos)

# Reemplazamos vacios por nan: 
reemplaza_vacios_x_nan(df6_order_reviews,'review_comment_title')
reemplaza_vacios_x_nan(df6_order_reviews,'review_comment_message')

# Modificamos el texto para que esté en formato título
str_a_titulo(df6_order_reviews,'review_comment_title')
str_a_titulo(df6_order_reviews,'review_comment_message')


#df7_orders

# Pasamos las columnas a formato fecha hora
columna_a_tipo_fecha_hora(df7_orders,'order_purchase_timestamp')
columna_a_tipo_fecha_hora(df7_orders,'order_approved_at')
columna_a_tipo_fecha_hora(df7_orders,'order_delivered_carrier_date')
columna_a_tipo_fecha_hora(df7_orders,'order_delivered_customer_date')
columna_a_tipo_fecha_hora(df7_orders,'order_estimated_delivery_date')

# 8_products:

#reemplazamos los guiones bajos por espacio
reemplzar_caracter_x_espacio(df8_products,'product_category_name','_')


# df9_sellers:

# Normalización de datos columna city
lista_1=['sao  paulo','sao paluo','sao paulo','sao paulo - sp', 'sao paulo / sao paulo', 'sao paulo sp', 'sao paulop','são paulo']
lista_2=['rio de janeiro, rio de janeiro, brasil','rio de janeiro \rio de janeiro', 'rio de janeiro / rio de janeiro']
lista_3=['riberao preto','ribeirao pretp', 'ribeirao preto / sao paulo']
lista_4=["santa barbara d oeste","santa barbara d´oeste"]
lista_5=['sao  jose dos pinhais','sao jose dos pinhas']
lista_6=['mogi das cruses','mogi das cruzes / sp']

replazar_datos(df9_sellers,'seller_city',lista_1,'sao paulo')
replazar_datos(df9_sellers,'seller_city',lista_2,'rio de janeiro')
replazar_datos(df9_sellers,'seller_city',lista_3,'ribeirao preto')
replazar_datos(df9_sellers,'seller_city',lista_4, "santa barbara d'oeste")
replazar_datos(df9_sellers,'seller_city',lista_5, "sao jose dos pinhais")
replazar_datos(df9_sellers,'seller_city',lista_6, 'mogi das cruzes')

replazar_datos(df9_sellers,'seller_city','novo hamburgo, rio grande do sul, brasil', 'novo hamburgo')
replazar_datos(df9_sellers,'seller_city','pinhais/pr', 'pinhais')
replazar_datos(df9_sellers,'seller_city',"arraial d'ajuda (porto seguro)", "arraial d'ajuda")
replazar_datos(df9_sellers,'seller_city','maua/sao paulo', 'maua')
replazar_datos(df9_sellers,'seller_city','lages - sc', 'lages')
replazar_datos(df9_sellers,'seller_city','sbc/sp', 'sbc')
replazar_datos(df9_sellers,'seller_city','sp / sp', 'sp')
replazar_datos(df9_sellers,'seller_city','carapicuiba / sao paulo', 'carapicuiba')
replazar_datos(df9_sellers,'seller_city','cariacica / es', 'cariacica')
replazar_datos(df9_sellers,'seller_city','jacarei / sao paulo', 'jacarei')
replazar_datos(df9_sellers,'seller_city',"sao miguel do oeste", "sao miguel d'oeste")
replazar_datos(df9_sellers,'seller_city','santo andre/sao paulo', 'santo andre')
replazar_datos(df9_sellers,'seller_city','vendas@creditparts.com.br', 'maringa')
replazar_datos(df9_sellers,'seller_city','04482255','rio de janeiro')

# 10_category_name:
#reemplazamos los guiones bajos por espacio, en ambas columnas
reemplzar_caracter_x_espacio(df10_category_name,'product_category_name','_')
reemplzar_caracter_x_espacio(df10_category_name,'product_category_name_english','_')

# Extraccion de csv: 

 # Se crea una lista con los url de destino
lista_url_destino=['C:/Users/AMD/Desktop/datasets_limpios/olist_01_marketing_qualified_leads_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_02_products_dataset.csv', 'C:/Users/AMD/Desktop/datasets_limpios/olist_03_product_category_name_translation_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_04_customers_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_05_sellers_dataset.csv', 'C:/Users/AMD/Desktop/datasets_limpios/olist_06_closed_deals_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_07_orders_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_08_order_items_dataset.csv', 'C:/Users/AMD/Desktop/datasets_limpios/olist_09_order_payments_dataset.csv','C:/Users/AMD/Desktop/datasets_limpios/olist_10_order_reviews_dataset.csv']
# Se crea una lista con los dataframe
lista_df=[df3_marketing_qualified_leads, df8_products, df10_category_name,df2_customers,df9_sellers,df1_closed_deals,df7_orders,df4_order_items, df5_order_payments, df6_order_reviews]
# Se extraen los csv a una carpeta de destino
for i in range(0,len(lista_url_destino)):
    exportar_csv(lista_df[i],lista_url_destino[i])

    