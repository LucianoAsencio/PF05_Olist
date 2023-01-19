# <h1 align=center> 📚 **Diccionario:** 📖 </h1>

<hr>  

# Índice  

+ [1- olist_customers_dataset.](#olist_customers_dataset)
+ [2- olist_order_items_dataset.](#olist_order_items_dataset)
+ [3- olist_order_payments_dataset.](#olist_order_payments_dataset)
+ [4- olist_order_reviews_dataset.](#olist_order_reviews_dataset)
+ [5- olist_orders_dataset.](#olist_orders_dataset)
+ [6- olist_products_dataset.](#olist_products_dataset)
+ [7- olist_sellers_dataset.](#olist_sellers_dataset)
+ [8- nombre_categoría_producto_traducción.](#nombre_categoría_producto_traducción)
+ [9- olist_closed_deals_dataset.](#olist_closed_deals_dataset)
+ [10- olist_marketing_qualified_leads_dataset.](#olist_marketing_qualified_leads_dataset)  

<hr>  

# olist_customers_dataset
Este conjunto de datos tiene información sobre el cliente y su ubicación. Se puede usar para identificar clientes únicos en el conjunto de datos de pedidos y para encontrar la ubicación de entrega de pedidos.   
Cantidad de registros: 99441

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | customer_id | Clave para el conjunto de datos de pedidos. Cada pedido tiene un ID de cliente único. | Varchar | 99441 |
| 2 | customer_zip_code_prefix | Código postal del cliente. | Int | 99441 |
| 3 | customer_city | Nombre de la ciudad del cliente. | Varchar | 99441 |
| 4 | customer_state | Estado donde vive el cliente. | Varchar | 99441 |

<hr>  

# olist_order_items_dataset
Este conjunto de datos incluye información sobre los artículos comprados en cada pedido, precio de venta y flete, cual fue su vendedor.   
Cantidad de registros: 112650

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | order_id | Identificador único del pedido. | Varchar | 112650 |
| 2 | order_item_id | Número secuencial que identifica el número de artículos incluidos en el mismo pedido. | Int | 112650 |
| 3 | product_id | Identificador único del producto. | Varchar | 112650 |
| 4 | seller_id | Identificador único del vendedor.  | Varchar | 112650 |
| 5 | shipping_limit_date | Fecha límite de envío del vendedor para entregar el pedido al socio logístico. | DateTime | 112650 |
| 6 | price | Precio del articulo. | Decimal | 112650 |
| 7 | freight_value | Precio del flete del articulo. | Decimal | 112650 |

<hr>  

# olist_order_payments_dataset
Este conjunto de datos incluye datos sobre las opciones de pago de los pedidos.  
Cantidad de registros: 103886

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | order_id | Identificador único de un pedido. | Varchar | 103886 |
| 2 | payment_sequential | Un cliente puede pagar un pedido con más de un método de pago. Si lo hace, se creará una secuencia para acomodar todos los pagos. | Int | 103886 |
| 3 | payment_type | Forma de pago elegida por el cliente. | Varchar | 103886 |
| 4 | payment_installments | Número de cuotas elegidas por el cliente. | Int | 103886 |
| 5 | payment_value | Valor de la transacción. | Decimal | 103886 |

<hr>  

# olist_order_reviews_dataset
Este conjunto de datos incluye datos sobre las criticas, ya sean buenas o malas, realizadas por los clientes.  
Cantidad de registros: 99224

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | review_id | Identificador de reseña único. | Varchar | 99224 |
| 2 | order_id | Identificador único de pedido. | Varchar | 99224 |
| 3 | review_score | Nota del 1 al 5 dada por el cliente en una encuesta de satisfacción.  | Int | 99224 |
| 4 | review_comment_title | Título del comentario de la reseña dejada por el cliente, en portugués. | Varchar | 11568 |
| 5 | review_comment_message | Mensaje de comentario de la reseña dejada por el cliente, en portugués. | Varchar | 40977 |
| 6 | review_creation_date | Fecha en que se envió la encuesta de satisfacción al cliente. | DateTime | 99224 |
| 7 | review_answer_timestamp | Marca de tiempo de la respuesta a la encuesta de satisfacción. | DateTime | 99224 |

<hr>  

# olist_orders_dataset
Este es el conjunto de datos central. De cada pedido puede encontrar toda la demás información.  
Cantidad de registros: 99441

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | order_id | Identificador único del pedido. | Varchar | 99441 |
| 2 | customer_id | Clave para el conjunto de datos del cliente. Cada pedido tiene un ID de cliente único.  | Varchar | 99441 |
| 3 | order_status | Referencia al estado del pedido (entregado, enviado, etc). | Varchar | 99441 |
| 4 | order_purchase_timestamp | Fecha de la compra. | DateTime | 99441 |
| 5 | order_approved_at | Fecha de aprobación del pago. | DateTime | 99281 |
| 6 | order_delivered_carrier_date | Fecha del pedido. Cuando se entregó al socio logístico. | DateTime | 97658 |
| 7 | order_delivered_customer_date | Fecha real de entrega del pedido al cliente. | DateTime | 96476 |
| 8 | order_estimated_delivery_date | Fecha estimada de entrega que fue informada al cliente en el momento de la compra. | DateTime | 99441 |

<hr>  

# olist_products_dataset
Este conjunto de datos incluye datos sobre los productos vendidos por Olist.  
Cantidad de registros: 32951

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | product_id | Identificador único de producto. | Varchar | 32951 |
| 2 | product_category_name | Categoría raíz del producto, en portugués. | Varchar | 32341 |
| 3 | product_name_length | Número de caracteres extraídos del nombre del producto.  | Decimal | 32341 |
| 4 | product_description_length | Número de caracteres extraídos de la descripción del producto.  | Decimal | 32341 |
| 5 | product_photos_qty | Número de fotos publicadas del producto. | Decimal | 32341 |
| 6 | product_weight_g | Peso del producto medido en gramos.  | Decimal | 32949 |
| 7 | product_length_cm | Longitud del producto medida en centímetros. | Decimal | 32949 |
| 8 | product_height_cm | Altura del producto medida en centímetros. | Decimal | 32949 |
| 9 | product_width_cm | Ancho del producto medido en centímetros. | Decimal | 32949 |

<hr>  

# olist_sellers_dataset
Este conjunto de datos incluye datos sobre los vendedores que cumplieron con los pedidos realizados en Olist. Incluye ubicación del vendedor.  
Cantidad de registros: 3095

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | seller_id | Identificador único del vendedor. | Varchar | 3095 |
| 2 | seller_zip_code_prefix | Código postal del vendedor. | Int | 3095 |
| 3 | seller_city | Nombre de la ciudad del vendedor. | Varchar | 3095 |
| 4 | seller_state | Estado del vendedor. | Varchar | 3095 |

<hr>  

# nombre_categoría_producto_traducción
Traduce product_category_name al inglés.    
Cantidad de registros: 71

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | product_category_name | Nombre de categoría en portugués. | Varchar | 71 |
| 2 | product_category_name_english | Nombre de categoría en inglés. | Varchar | 71 |

<hr>  

# olist_closed_deals_dataset
Este es un conjunto de datos de embudo de marketing de vendedores que completaron solicitudes de contacto para vender sus productos en Olist Store, que solicitaron contacto entre el 1 de junio de 2017 y el 1 de junio de 2018.  
Cantidad de registros: 842

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | closed_deals_id | Identificador de cada trato de closed deals | Varchar | 842 | 
| 2 | mql_id | Identificador unico de "Clientes potenciales calificados de marketing". | Varchar | 842 |
| 3 | seller_id | Identificador único del vendedor. | Varchar | 842 |
| 4 | sdr_id | Identificador de representante de desarrollo de ventas. El SDR ayuda a confirmar algunas informaciones y programar una consultoría. | Varchar | 842 |
| 5 | sr_id | Identificador de Representante de Ventas. El SR puede cerrar el trato (el cliente potencial se registra) o perder el trato (el líder se va sin iniciar sesión). | Varchar | 842 |
| 6 | won_date | Fecha en que se cerró el trato. | Varchar | 842 |
| 7 | business_segment | Segmento del mercado en el que se va a desarrollar sus ventas. | Varchar | 841 |
| 8 | lead_type | Estos valores indican diferentes tipos o categorías de leads. | Varchar | 836 |
| 9 | lead_behaviour_profile | Está relacionado con la prueba de personalidad DISC. Tiburón - Dominio, Águila - Influencia, Gato - Estabilidad, Lobo - Conciencia. | Varchar | 665 |
| 10 | business_type | Estos valores indican diferentes tipos de negocios o categorías de empresas por ej (revendedor, fabricante). | Varchar | 832 |

<hr>  

# olist_marketing_qualified_leads_dataset
Este conjunto de datos hace referencia a como el posible cliente entro en contacto a traves del marketing.
Cantidad de registros: 8000

| # | Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| - | -------- | ----------- | :----------: | :------------------: |
| 1 | mql_id | Identificador unico de "Clientes potenciales calificados de marketing". | Varchar | 8000 |
| 2 | first_contact_date | Fecha del primer contacto con el anuncio de olist. | DateTime | 8000 |
| 3 | landing_page_id | Destino al que fue al hacer click en el anuncio. | Varchar | 8000 |
| 4 | origin | Tipo de marketing que se uso (organico, pago, etc.). | Varchar | 7940 |
