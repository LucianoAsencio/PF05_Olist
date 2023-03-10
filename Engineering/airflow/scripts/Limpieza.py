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
Es una table incompleta a pesar de su dimensión ya que no tiene todos
los zip_code (códigos postales) presentes en las tablas de Customers 
y Sellers por lo tanto será eliminada del modelo.
Se evaluará hacer una nueva tabla de geolocation sin latitud
ni longitud, según su posible utilidad. 
### 4_marketing_q_leads:
Se pasan la siguiente columna a formato fecha hora:
 - 'first_contact_date'
### 5_order_items:
Se pasan la siguiente columna a formato fecha hora:
 - 'shipping_limit_date'
 
### 6_order_payments:
Se cambia de formato a entero: 
 - 'payment_installments'
### 7_order_reviews:
Se pasan las siguientes columnas a formato fecha hora:
 - 'review_creation_date'
 - 'review_answer_timestamp'
### 8_orders:
Se pasan las siguientes columnas a formato fecha hora: 
 - 'order_purchase_timestamp'
 - 'order_approved_at'
 - 'order_delivered_carrier_date'
 - 'order_delivered_customer_date'
 - 'order_estimated_delivery_date'
### 9_products:
 -  sin modificaciones
### 10_sellers:
 - sin modificaciones
### 11_product_category_name_translation:
 - sin modificaciones
'''

#_____________________________________________________________

#Importamos las librerias y funciones: 

import pandas as pd
import secrets
from funciones_ETL import *

# Abrimos los datasets desde una supuesta API

df1_closed_deals= pd.read_csv('www.fakeapi.com/dataset/closed_deals.csv')
df2_customers=pd.read_csv('www.fakeapi.com/dataset/olist_customers_dataset.csv')
df4_marketing_qualified_leads=pd.read_csv('www.fakeapi.com/dataset/olist_marketing_qualified_leads_dataset.csv')
df5_order_items=pd.read_csv('www.fakeapi.com/dataset/olist_order_items_dataset.csv')
df6_order_payments=pd.read_csv('www.fakeapi.com/dataset/olist_order_payments_dataset.csv')
df7_order_reviews=pd.read_csv('www.fakeapi.com/dataset/olist_order_reviews_dataset.csv')
df8_orders=pd.read_csv('www.fakeapi.com/dataset/olist_orders_dataset.csv')
df9_products=pd.read_csv('www.fakeapi.com/dataset/olist_products_dataset.csv')
df10_sellers=pd.read_csv('www.fakeapi.com/dataset/olist_sellers_dataset.csv')
df11_category_name=pd.read_csv('www.fakeapi.com/dataset/product_category_name_translation.csv')

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
lista_ids = df10_sellers['seller_id'].unique()

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
columna_a_tipo_fecha_hora(df4_marketing_qualified_leads,'first_contact_date')


# 4_order_items:

# Pasamos a formato la fecha con hora
columna_a_tipo_fecha_hora(df5_order_items,'shipping_limit_date')


# 5_order_payments:

# Cambio de tipo de dato a entero
columna_a_tipo_entero(df6_order_payments,'payment_installments')


# 6_order_reviews:

# Cambiamos a formato fecha la columna  review_creation_date
columna_a_tipo_fecha_hora(df7_order_reviews,'review_creation_date')
columna_a_tipo_fecha_hora(df7_order_reviews,'review_answer_timestamp')


# 7_orders:

# Pasamos las columnas a formato fecha hora
columna_a_tipo_fecha_hora(df8_orders,'order_purchase_timestamp')
columna_a_tipo_fecha_hora(df8_orders,'order_approved_at')
columna_a_tipo_fecha_hora(df8_orders,'order_delivered_carrier_date')
columna_a_tipo_fecha_hora(df8_orders,'order_delivered_customer_date')
columna_a_tipo_fecha_hora(df8_orders,'order_estimated_delivery_date')

# 8_sellers:
# Normalización de datos columna city
lista_1=['sao  paulo','sao paluo','sao paulo','sao paulo - sp', 'sao paulo / sao paulo', 'sao paulo sp', 'sao paulop','são paulo']
lista_2=['rio de janeiro, rio de janeiro, brasil','rio de janeiro \rio de janeiro', 'rio de janeiro / rio de janeiro']
lista_3=['riberao preto','ribeirao pretp', 'ribeirao preto / sao paulo']
lista_4=["santa barbara d oeste","santa barbara d´oeste"]
lista_5=['sao  jose dos pinhais','sao jose dos pinhas']
lista_6=['mogi das cruses','mogi das cruzes / sp']

replazar_datos(lista_1,'sao paulo')
replazar_datos(lista_2,'rio de janeiro')
replazar_datos(lista_3,'ribeirao preto')
replazar_datos(lista_4, "santa barbara d'oeste")
replazar_datos(lista_5, "sao jose dos pinhais")
replazar_datos(lista_6, 'mogi das cruzes')

replazar_datos('novo hamburgo, rio grande do sul, brasil', 'novo hamburgo')
replazar_datos('pinhais/pr', 'pinhais')
replazar_datos("arraial d'ajuda (porto seguro)", "arraial d'ajuda")
replazar_datos('maua/sao paulo', 'maua')
replazar_datos('lages - sc', 'lages')
replazar_datos('sbc/sp', 'sbc')
replazar_datos('sp / sp', 'sp')
replazar_datos('carapicuiba / sao paulo', 'carapicuiba')
replazar_datos('cariacica / es', 'cariacica')
replazar_datos('jacarei / sao paulo', 'jacarei')
replazar_datos("sao miguel do oeste", "sao miguel d'oeste")
replazar_datos('santo andre/sao paulo', 'santo andre')


#Con respecto a las tablas 8_sellers 9_products y 10_category_name No se realizaron cambios

# Extraccion de csv: 

 # Se crea una lista con los url de destino
lista_url_destino=['/home/ubuntu/registros/olist_01_marketing_qualified_leads_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_02_products_dataset.csv', '/home/ubuntu/registros/datasets_limpios/olist_03_product_category_name_translation_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_04_customers_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_05_sellers_dataset.csv', '/home/ubuntu/registros/datasets_limpios/olist_06_closed_deals_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_07_orders_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_08_order_items_dataset.csv', '/home/ubuntu/registros/datasets_limpios/olist_09_order_payments_dataset.csv','/home/ubuntu/registros/datasets_limpios/olist_10_order_reviews_dataset.csv']
# Se crea una lista con los dataframe
lista_df=[df4_marketing_qualified_leads, df9_products, df11_category_name,df2_customers,df10_sellers,df1_closed_deals,df8_orders,df5_order_items,df6_order_payments,df7_order_reviews]
# Se extraen los csv a una carpeta de destino
for i in range(0,len(lista_url_destino)):
    exportar_csv(lista_df[i],lista_url_destino[i])