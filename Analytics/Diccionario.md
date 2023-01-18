## Diccionario:  
### Formato:  

Tabla    
descripcion.      
- Columna: descripcion   

<hr>  

### olist_customers_dataset   
Este conjunto de datos tiene información sobre el cliente y su ubicación. Se puede usar para identificar clientes únicos en el conjunto de datos de pedidos y para encontrar la ubicación de entrega de pedidos.  

- `customer_id:` clave para el conjunto de datos de pedidos. Cada pedido tiene un ID de cliente único.  
- `customer_unique_id:` identificador único de un cliente.  
- `customer_zip_code_prefix:` código postal del cliente.  
- `customer_city:` Nombre de la ciudad del cliente.  
- `customer_state:` Estado donde vive el cliente.  

### olist_geolocalización_dataset  
Este conjunto de datos contiene información sobre los códigos postales de Brasil y sus coordenadas de latitud y longitud.  

- `geolocation_zip_code_prefix:` código postal.  
- `geolocation_lat:` latitud.  
- `geolocation_lng:` longitud.  
- `geolocation_city:` Nombre de la ciudad.  
- `geolocation_state:` Abreviacion del nombre del Estado.  

### olist_order_items_dataset  
Este conjunto de datos incluye información sobre los artículos comprados en cada pedido, precio de venta y flete, cual fue su vendedor.  


- `order_id:` identificador único del pedido.  
- `order_item_id:` número secuencial que identifica el número de artículos incluidos en el mismo pedido.  
- `product_id:` identificador único del producto.  
- `seller_id:` identificador único del vendedor.  
- `shipping_limit_date:` muestra la fecha límite de envío del vendedor para entregar el pedido al socio logístico.  
- `price:` precio del articulo.  
- `freight_value:` precio del flete del articulo.  

### olist_order_payments_dataset  
Este conjunto de datos incluye datos sobre las opciones de pago de los pedidos.  

- `order_id:` identificador único de un pedido.  
- `payment_sequential:` un cliente puede pagar un pedido con más de un método de pago. Si lo hace, se creará una secuencia para acomodar todos los pagos.  
- `payment_type:` forma de pago elegida por el cliente.  
- `payment_installments:` número de cuotas elegidas por el cliente.  
- `payment_value:` valor de la transacción.  

### olist_order_reviews_dataset  
Este conjunto de datos incluye datos sobre las criticas, ya sean buenas o malas, realizadas por los clientes.  


- `review_id:` identificador de reseña único.  
- `order_id:` identificador único de pedido.  
- `review_score:` Nota del 1 al 5 dada por el cliente en una encuesta de satisfacción.  
- `review_comment_title:` Título del comentario de la reseña dejada por el cliente, en portugués.  
- `review_comment_message:` Mensaje de comentario de la reseña dejada por el cliente, en portugués.  
- `review_creation_date:` Muestra la fecha en que se envió la encuesta de satisfacción al cliente.  
- `review_answer_timestamp:` Muestra la marca de tiempo de la respuesta a la encuesta de satisfacción.  


### olist_orders_dataset  
Este es el conjunto de datos central. De cada pedido puede encontrar toda la demás información.  

- `rder_id:` identificador único del pedido.  
- `customer_id:` clave para el conjunto de datos del cliente. Cada pedido tiene un ID de cliente único.  
- `order_status:` Referencia al estado del pedido (entregado, enviado, etc).  
- `order_purchase_timestamp:` Muestra la fecha de la compra.  
- `order_approved_at:` Muestra la fecha de aprobación del pago.  
- `order_delivered_carrier_date:` Muestra la fecha del pedido. Cuando se entregó al socio logístico.  
- `order_delivered_customer_date:` Muestra la fecha real de entrega del pedido al cliente.  
- `order_estimated_delivery_date:` Muestra la fecha estimada de entrega que fue informada al cliente en el momento de la compra.  


### olist_products_dataset  
Este conjunto de datos incluye datos sobre los productos vendidos por Olist.  

- `product_id:` identificador único de producto.  
- `product_category_name:` categoría raíz del producto, en portugués.  
- `product_name_length:` número de caracteres extraídos del nombre del producto.  
- `product_description_length:` número de caracteres extraídos de la descripción del producto.  
- `product_photos_qty:` número de fotos publicadas del producto.  
- `product_weight_g:` peso del producto medido en gramos.  
- `product_length_cm:` longitud del producto medida en centímetros.  
- `product_height_cm:` altura del producto medida en centímetros.  
- `product_width_cm:` ancho del producto medido en centímetros.  

### olist_sellers_dataset  
Este conjunto de datos incluye datos sobre los vendedores que cumplieron con los pedidos realizados en Olist. Incluye ubicación del vendedor.  

- `seller_id:` identificador único del vendedor.  
- `seller_zip_code_prefix:` código postal del vendedor.  
- `seller_city:` nombre de la ciudad del vendedor.  
- `seller_state:` estado del vendedor.  

### nombre_categoría_producto_traducción  
Traduce product_category_name al inglés.  

- `product_category_name:` nombre de categoría en portugués.   
- `product_category_name_english:` nombre de categoría en inglés.    


### olist_closed_deals_dataset   
Este es un conjunto de datos de embudo de marketing de vendedores que completaron solicitudes de contacto para vender sus productos en Olist Store, que solicitaron contacto entre el 1 de junio de 2017 y el 1 de junio de 2018.  

- `mql_id:` identificador unico de "Clientes potenciales calificados de marketing".  
- `seller_id:` identificador único del vendedor.  
- `sdr_id:` identificador de  representante de desarrollo de ventas. El SDR ayuda a confirmar algunas informaciones y programar una consultoría.  
- `sr_id:` identificador de Representante de Ventas. El SR puede cerrar el trato (el cliente potencial se registra) o perder el trato (el líder se va sin iniciar sesión).  
- `won_date:` fecha en que se cerró el trato.  
- `business_segment:` segmento del mercado en el que se va a desarrollar sus ventas.  
- `lead_type:` estos valoresindican diferentes tipos o categorías de leads.  
- `lead_behaviour_profile:`Está relacionado con la prueba de personalidad DISC. Tiburón - Dominio, Águila - Influencia, Gato - Estabilidad, Lobo - Conciencia.  
- `business_type:` estos valores indican diferentes tipos de negocios o categorías de empresas por ej (revendedor, fabricante).  

### olist_marketing_qualified_leads_dataset
Este conjunto de datos hace referencia a como el posible cliente entro en contacto a traves del marketing.  

- `mql_id:` identificador unico de "Clientes potenciales calificados de marketing".  
- `first_contact_date:` fecha del primer contacto con el anuncio de olist.  
- `landing_page_id:` destino al que fue al hacer click en el anuncio.  
- `origin:` tipo de marketing que se uso (organico, pago, etc.).  