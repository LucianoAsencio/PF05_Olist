# <h1 align=center>  **Informe ETL**  </h1>
<hr>  

![imagen](https://cdn-icons-png.flaticon.com/128/1766/1766865.png)

# Índice  

+ [Resumen](#performance_ventas)  
+ [Limpieza y normalización de tablas](#logistica)  
+ [Pareto dinamico vendedores.](#pareto_dinamico_vendedores)  


<hr>  


## Resumen:  
Se ha realizado un ETL versátil, el mismo comienza tomado los archivos de una carpeta local llamada datasets, los mismos puede abrirse con una fórmula que admite múltiples formatos de archivo, sin embargo, la misma queda para ser activada en una segunda instancia, ya que ralentiza el proceso de ETL y no se requiere por el momento, dado que todos los datasets se encuentran en formato csv.

El proceso se encuentra en formato de python (.py) que será llamada y ejecutado automáticamente siempre que se generen nuevas cargas de archivo a las carpetas destinadas para tal fin [carga incremental]. 

El script principal [ETL_Olist.py] se vincula con el archivo [funciones_ETL.py] para dejar el ETL principal más limpio y corto.

## Limpieza y normalización tabla por tabla:

### Tablas: 

- 1 olist_closed_deals_dataset.csv
- 2 olist_customers_dataset.csv
- 3 olist_geolocation_dataset.csv
- 4 olist_marketing_qualified_leads_dataset.csv
- 5 olist_order_items_dataset.csv
- 6 olist_order_payments_dataset.csv
- 7 olist_order_reviews_dataset.csv
- 8 olist_orders_dataset.csv
- 9 olist_products_dataset.csv
- 10 olist_sellers_dataset.csv
- 11 product_category_name_translation.csv


### TABLA 1_closed_deals

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **won_date** | - | - | - | - | a Date time type| 
| 2 | **business_segment** | - | se mantienen en NaN los datos faltantes (1%) - pasan a NULL en MySQL| - | - | - |
| 3 | **lead_type** | - | se mantienen en NaN los datos faltantes (1%) - pasan a NULL en MySQL| - | - | - | número de órdenes del año anterior y comparando con la meta establecida |
| 4 | **lead_behaviour_profile** | - | se mantienen en NaN los datos faltantes (21%) - pasan a NULL en MySQL| - | - | - | número de órdenes del año anterior y comparando con la meta establecida |
| 5 | **has_company** | Si | - | - | - | - | 
| 6 | **has_gtin** | Si | - | - | - | - | 
| 7 | **average_stock** | Si | - | - | - | - | 
| 8 | **business_type** | - | se mantienen en NaN los datos faltantes (1%) - pasan a NULL en MySQL | - | - | - | 
| 9 | **declared_product_catalog_size** | Si | - | - | - | - | 
| 10 | **declared_monthly_reven** | Si | - | - | - | - | 
| 11 | **closed_deals_id** | CREAR NUEVA COLUMNA | - | - | - | - | 


<hr>

### TABLA 2_customers:  

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **customer_unique_id** | Si | - | - | - | - | 


<hr>

### TABLA 3 _geolocations:   

Es una table incompleta a pesar de su dimensión ya que no tiene todos los zip_code (códigos postales) presentes en las tablas de Customers y Sellers por lo tanto será eliminada del modelo y se evaluará hacer una nueva tabla de geolocation sin latitud ni longitud, según su posible utilidad.

### TABLA 4 _marketing_quality_leads: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |    
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **first_contact_date** | - | - | - | - | a formato date  |  
| 2 | **origin** | - | se mantienen en NaN los datos faltantes (1%) - pasan a NULL en MySQL | - | - | - |    

<hr>

### TABLA 5 _order_items:

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **shipping_limit_date**| - | - | Se modifican 3 datos que poseen mal la fecha (la fecha se trae por order id de otra tabla) | - | a Date time type | 
| 2 | **price** | - | -| No se modifica el separador _ se realizará sobre Power Bi | - | tipo de dato a decimal |
| 3 | **freight_value** | - | -| No se modifica el separador _ se realizará sobre Power Bi | - | tipo de dato a decimal |


### TABLA 6 _order_payments: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** | 
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **pyment_value** | - | - | NO se modifica el separador _ se realizará sobre Power Bi | - | tipo de dato a decimal | 
| 2 | **payment_installments** | - | -| - | - | tipo de dato a entero |

### TABLA 7 _order_reviews: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |   
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **review_comment_title** | - | se mantienen en NaN los datos faltantes (88%) - pasan a NULL en MySQL y se limpian todos los datos_normalizando | - | Corrección de datos, desde simbolos hasta normalización en formato título - Se conservaron los emojis para posterior posible uso en analisis de sentimientos | - | 
| 2 | **review_comment_message** | - | sse mantienen en NaN los datos faltantes (56%) - pasan a NULL en MySQL y se limpian todos los datos_normalizando | - | Corrección de datos, desde simbolos hasta normalización en formato título - Se conservaron los emojis para posterior posible uso en analisis de sentimientos | - |
| 3 | **review_creation_date** | - | - | - | - | - |  tipo de dato a fecha hora |
| 4 | **review_answer_timestamp** | - | - | - | - | - |  tipo de dato a fecha hora |

### TABLA 8 _orders: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **order_purchase_timestamp** | - | - | - | - | tipo de dato a fecha  hora| 
| 2 | **order_approved_at** | - | sse mantienen en NaN los datos faltantes (0,2%)- pasan a NULL en MySQL| - | - | tipo de dato a fecha  hora|
| 3 | **order_delivered_carrier_date** | - | se mantienen en NaN los datos faltantes (1,8%)- pasan a NULL en MySQL  | - | - | - | tipo de dato a fecha  hora |
| 4 | **order_delivered_customer_date** | - | sse mantienen en NaN los datos faltantes (3%)- pasan a NULL en MySQL | - | - | - | tipo de dato a fecha  hora |
| 5 | **order_estimated_delivery_date** | - | - | - | - | tipo de dato a fecha  hora | 

### TABLA 9 _product: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **producto_category_name** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - | 
| 2 | **product_name_lenght** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - |
| 3 | **product_description_lenght** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL  | - | - | - | - |
| 4 | **product_photos_qty** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - | - |
| 5 | **product_weight_g** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - | 
| 6 | **product_length_cm** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - | 
| 7 | **product_height_cm** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - | - | 
| 8 | **product_width_cm** | - | se mantienen en NaN los datos faltantes - pasan a NULL en MySQL | - | - |  - | 


### TABLA 10 _sellers: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **sellers city** | - | se homogenizaron todos los errores presentados en cuanto a la escritura de las ciudades. Ver scrip para más detalles | - | - | - | 

### TABLA 11 _category_name: 

| # | **Columna** | **Eliminada** | **Datos Completos** |  **Datos Corregidos**  |  **Datos Normalizados** | **Cambio de Tipo de Dato** |  
| - | -------- | ----------- | ---------- | --------|--------|--------|
| 1 | **product_category_name** | - | - | - | nomalización reemplazando guion bajo por espacio | - | 
| 2 | **product_category_name_english** | - | - | - | nomalización reemplazando guion bajo por espacio | - | 


## Resumen:

<aside>
💡 11 Total tablas:

Las modificaciones a realizar para obtener datos limpios para el Data Warehouse son:

### **1_closed_deals**:

- 'won_date' _ cambio de formato a fecha hora

Se eliminan las columnas por falta de datos suficientes (NaN o 0):

- 'has_gtin'
- 'has_company'
- 'average_stock'
- 'declared_product_catalog_size'
- 'declared_monthly_revenue'

Se crea un nuevo id en una nueva columna que se coloca al inicio de la tabla.

- 'closed_deals_id'

### **2_customers**:

Se elimina la columna de customer_unique_id porque no es un id único:

- 'customer_unique_id'

### **3_geolocation**:

Es una table incompleta a pesar de su dimensión ya que no tiene todos los zip_code (códigos postales) presentes en las tablas de Customers y Sellers por lo tanto será eliminada del modelo y se evaluará hacer una nueva tabla de geolocation sin latitud ni longitud, según su posible utilidad.

### **4_marketing_q_leads**:

Se pasan la siguiente columna a formato fecha hora:

- 'first_contact_date'

### **5_order_items**:

Se pasan la siguiente columna a formato fecha hora:

- 'shipping_limit_date'

Se reemplazan 4 fechas que estan situadas en 2020, reemplazando los valores según el ID de orden de la tabla order por la fecha correcta

### **6_order_payments**:

Se cambia de formato a entero:

- 'payment_installments'

### **7_order_reviews**:

Se pasan las siguientes columnas a formato fecha hora:

- 'review_creation_date'
- 'review_answer_timestamp'

Se limpian las columnas del texto title y comments de reviews

- 'review_comment_title'
- 'review_comment_message'

### **8_orders**:

Se pasan las siguientes columnas a formato fecha hora:

- 'order_purchase_timestamp'
- 'order_approved_at'
- 'order_delivered_carrier_date'
- 'order_delivered_customer_date'
- 'order_estimated_delivery_date'

### **9_product**:

Se quitaron los guiones bajos y se reemplazar por espacios:

- 'product_category_name'

### **10_sellers**:

Se agrega normalizan los datos de la columa:

- 'seller_city'

### **11_category_name**:

Se quitaron los guiones bajos y se reemplazar por espacios:

- 'product_category_name'
- 'product_category_name_english'
</aside>


# Conclusion
Como conclusión podemos expresar que los nombres de las columnas se encuentran normalizados en inglés, que los id están estandarizados a 32 dígitos alfanuméricos y que se generó el id de la tabla 1 _closed_deals, siguiendo el mismo formato. 

Se incorporó el formato de fecha y hora en todas las columnas que poseen fechas, con el fin de vincularlas con una tabla calendario en MySQL. 

Los valores nulos se conservaron como tal, ya que MySQL podrá tomar los valores NaN como NULL y nos permitirá contar con información de los valores nulos a la vez que conservar el formato de las columnas sin alterar el mismo.