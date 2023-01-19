# <h1 align=center> 📚 **Diccionario:** 📖 </h1>

<hr>  

### Índice  

+ [1- olist_customers_dataset.](#olist_customers_dataset)
+ [2- olist_geolocation_dataset.](#olist_geolocation_dataset)
+ [3- olist_order_items_dataset.](#olist_order_items_dataset)
+ [4- olist_order_payments_dataset.](#olist_order_payments_dataset)
+ [5- olist_order_reviews_dataset.](#olist_order_reviews_dataset)
+ [6- olist_orders_dataset.](#olist_orders_dataset)
+ [7- olist_products_dataset.](#olist_products_dataset)
+ [8- olist_sellers_dataset.](#olist_sellers_dataset)
+ [9- nombre_categoría_producto_traducción.](#nombre_categoría_producto_traducción)
+ [10- olist_closed_deals_dataset.](#olist_closed_deals_dataset)
+ [11- olist_marketing_qualified_leads_dataset.](#olist_marketing_qualified_leads_dataset)  

<hr>  

### olist_customers_dataset
Este conjunto de datos tiene información sobre el cliente y su ubicación. Se puede usar para identificar clientes únicos en el conjunto de datos de pedidos y para encontrar la ubicación de entrega de pedidos.   


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| customer_id | Clave para el conjunto de datos de pedidos. Cada pedido tiene un ID de cliente único. |  |  |
| customer_unique_id | Identificador único de un cliente. |  |  |
| customer_zip_code_prefix | Código postal del cliente. |  |  |
| customer_city | Nombre de la ciudad del cliente. |  |  |
| customer_state | Estado donde vive el cliente. |  |  |

<hr>  

### olist_geolocation_dataset
Este conjunto de datos contiene información sobre los códigos postales de Brasil y sus coordenadas de latitud y longitud.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| geolocation_zip_code_prefix | Código postal. |  |  |
| geolocation_lat | Latitud. |  |  |
| geolocation_lng | Longitud. |  |  |
| geolocation_city | Nombre de la ciudad. |  |  |
| geolocation_state | Abreviacion del nombre del Estado. |  |  |

<hr>  

### olist_order_items_dataset
Este conjunto de datos incluye información sobre los artículos comprados en cada pedido, precio de venta y flete, cual fue su vendedor.   


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| order_id | Identificador único del pedido. |  |  |
| order_item_id | Número secuencial que identifica el número de artículos incluidos en el mismo pedido. |  |  |
| product_id | Identificador único del producto. |  |  |
| seller_id | Identificador único del vendedor.  |  |  |
| shipping_limit_date | Fecha límite de envío del vendedor para entregar el pedido al socio logístico. |  |  |
| price | Precio del articulo. |  |  |
| freight_value | Precio del flete del articulo. |  |  |

<hr>  

### olist_order_payments_dataset
Este conjunto de datos incluye datos sobre las opciones de pago de los pedidos.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| order_id | Identificador único de un pedido. |  |  |
| payment_sequential | Un cliente puede pagar un pedido con más de un método de pago. Si lo hace, se creará una secuencia para acomodar todos los pagos. |  |  |
| payment_type | Forma de pago elegida por el cliente. |  |  |
| payment_installments | Número de cuotas elegidas por el cliente. |  |  |
| payment_value | Valor de la transacción. |  |  |

<hr>  

### olist_order_reviews_dataset
Este conjunto de datos incluye datos sobre las criticas, ya sean buenas o malas, realizadas por los clientes.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| review_id | Identificador de reseña único.   |  |  |
| order_id | Identificador único de pedido. |  |  |
| review_score | Nota del 1 al 5 dada por el cliente en una encuesta de satisfacción.  |  |  |
| review_comment_title | Título del comentario de la reseña dejada por el cliente, en portugués. |  |  |
| review_comment_message | Mensaje de comentario de la reseña dejada por el cliente, en portugués. |  |  |
| review_creation_date | Fecha en que se envió la encuesta de satisfacción al cliente. |  |  |
| review_answer_timestamp | Marca de tiempo de la respuesta a la encuesta de satisfacción. |  |  |

<hr>  

### olist_orders_dataset
Este es el conjunto de datos central. De cada pedido puede encontrar toda la demás información.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| order_id | Identificador único del pedido. |  |  |
| customer_id | Clave para el conjunto de datos del cliente. Cada pedido tiene un ID de cliente único.  |  |  |
| order_status | Referencia al estado del pedido (entregado, enviado, etc). |  |  |
| order_purchase_timestamp | Fecha de la compra. |  |  |
| order_approved_at | Fecha de aprobación del pago. |  |  |
| order_delivered_carrier_date | Fecha del pedido. Cuando se entregó al socio logístico. |  |  |
| order_delivered_customer_date | Fecha real de entrega del pedido al cliente. |  |  |
| order_estimated_delivery_date | Fecha estimada de entrega que fue informada al cliente en el momento de la compra. |  |  |

<hr>  

### olist_products_dataset
Este conjunto de datos incluye datos sobre los productos vendidos por Olist.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| product_id | Identificador único de producto. |  |  |
| product_category_name | Categoría raíz del producto, en portugués. |  |  |
| product_name_length | Número de caracteres extraídos del nombre del producto.  |  |  |
| product_description_length | Número de caracteres extraídos de la descripción del producto.  |  |  |
| product_photos_qty | Número de fotos publicadas del producto.   |  |  |
| product_weight_g | Peso del producto medido en gramos.  |  |  |
| product_length_cm | Longitud del producto medida en centímetros. |  |  |
| product_height_cm | Altura del producto medida en centímetros. |  |  |
| product_width_cm | Ancho del producto medido en centímetros. |  |  |

<hr>  

### olist_sellers_dataset
Este conjunto de datos incluye datos sobre los vendedores que cumplieron con los pedidos realizados en Olist. Incluye ubicación del vendedor.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| seller_id | Identificador único del vendedor. |  |  |
| seller_zip_code_prefix | Código postal del vendedor. |  |  |
| seller_city | Nombre de la ciudad del vendedor. |  |  |
| seller_state | Estado del vendedor. |  |  |

<hr>  

### nombre_categoría_producto_traducción
Traduce product_category_name al inglés.    


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| product_category_name | Nombre de categoría en portugués. |  |  |
| product_category_name_english | Nombre de categoría en inglés. |  |  |

<hr>  

### olist_closed_deals_dataset
Este es un conjunto de datos de embudo de marketing de vendedores que completaron solicitudes de contacto para vender sus productos en Olist Store, que solicitaron contacto entre el 1 de junio de 2017 y el 1 de junio de 2018.  


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| mql_id | Identificador unico de "Clientes potenciales calificados de marketing". |  |  |
| seller_id | Identificador único del vendedor. |  |  |
| sdr_id | Identificador de representante de desarrollo de ventas. El SDR ayuda a confirmar algunas informaciones y programar una consultoría. |  |  |
| sr_id | Identificador de Representante de Ventas. El SR puede cerrar el trato (el cliente potencial se registra) o perder el trato (el líder se va sin iniciar sesión). |  |  |
| won_date | Fecha en que se cerró el trato. |  |  |
| business_segment | Segmento del mercado en el que se va a desarrollar sus ventas. |  |  |
| lead_type | Estos valores indican diferentes tipos o categorías de leads. |  |  |
| lead_behaviour_profile | Está relacionado con la prueba de personalidad DISC. Tiburón - Dominio, Águila - Influencia, Gato - Estabilidad, Lobo - Conciencia. |  |  |
| business_type | Estos valores indican diferentes tipos de negocios o categorías de empresas por ej (revendedor, fabricante). |  |  |

<hr>  

### olist_marketing_qualified_leads_dataset
Este conjunto de datos hace referencia a como el posible cliente entro en contacto a traves del marketing.


| Columnas | Descripción | Tipo de Dato | Registros (Not Null) |
| -------- | ----------- | ------------ | -------------------- |
| mql_id | Identificador unico de "Clientes potenciales calificados de marketing". |  |  |
| first_contact_date | Fecha del primer contacto con el anuncio de olist. |  |  |
| landing_page_id | Destino al que fue al hacer click en el anuncio. |  |  |
| origin | Tipo de marketing que se uso (organico, pago, etc.). |  |  |
