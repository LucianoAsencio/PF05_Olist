use olist_pf;
-- Limpieza sobre la columna sellers_city en tabla sellers
/*
# Se ajustan las ciudades a "sao paulo" en una lista de ciudades con diferente formato
UPDATE sellers
SET seller_city = 'sao paulo'
WHERE seller_city IN ('sao  paulo','sao paluo','sao paulo','sao paulo - sp', 'sao paulo / sao paulo', 'sao paulo sp', 'sao paulop','são paulo')
AND seller_state = 'SP';

# Se ajustan las ciudades a "sao jose do rio preto" en una lista de ciudades con diferente formato
UPDATE sellers
SET seller_city = "sao jose do rio preto"
WHERE seller_city IN ("sao jose do rio pret")
AND seller_state = "SP";

# Hay varios valores que tienen un error en el que ponen una barra ("/") y a su lado el nombre del estado o las iniciales
# Esta fórmula reemplaza aquellos datos con todo su contenido antes de la barra.
UPDATE sellers
SET seller_city = SUBSTRING_INDEX(seller_city, '/', 1);

# Lo mismo pero la barra es invertida ("\")
UPDATE sellers
SET seller_city = SUBSTRING_INDEX(seller_city, '\\', 1);
*/

#se limpian los datos mal escritos: 

UPDATE sellers
SET seller_city = 'rio de janeiro'
WHERE seller_city IN ('rio de janeiro, rio de janeiro, brasil','rio de janeiro \rio de janeiro', 'rio de janeiro / rio de janeiro');

UPDATE sellers
SET seller_city = 'ribeirao preto'
WHERE seller_city IN ('riberao preto','ribeirao pretp', 'ribeirao preto / sao paulo');

UPDATE sellers
SET seller_city = "santa barbara d'oeste"
WHERE seller_city IN ("santa barbara d oeste","santa barbara d´oeste");

UPDATE sellers
SET seller_city = "sao jose dos pinhais"
WHERE seller_city IN ('sao  jose dos pinhais','sao jose dos pinhas');

UPDATE sellers
SET seller_city = 'mogi das cruzes'
WHERE seller_city IN ('mogi das cruses','mogi das cruzes / sp');

UPDATE sellers
SET seller_city = 'novo hamburgo'
WHERE seller_city = 'novo hamburgo, rio grande do sul, brasil';

UPDATE sellers
SET seller_city = "arraial d'ajuda"
WHERE seller_city = "arraial d'ajuda (porto seguro)";

UPDATE sellers
SET seller_city = 'lages'
WHERE seller_city = 'lages - sc';

UPDATE sellers
SET seller_city = "sao miguel d'oeste"
WHERE seller_city = "sao miguel do oeste";

-- se corrigen 4 fechas que estan mal cargadas en order_items
UPDATE order_items
SET shipping_limit_date = "2017-06-09 13:35:54"
WHERE shipping_limit_date = "2020-04-09 22:35:08";

UPDATE order_items
SET shipping_limit_date = NULL
WHERE shipping_limit_date = "2020-02-05 03:30:51";

UPDATE order_items
SET shipping_limit_date = "2017-08-04 00:00:00"
WHERE shipping_limit_date = "2020-02-03 20:23:22";


-- Se limpia la columna product_category_name_english (de la tabla Product_category_name_translation)
UPDATE product_category_name_translation as cp
SET cp.product_category_name_english = REPLACE(cp.product_category_name_english, '_', ' ')
WHERE cp.product_category_name_english LIKE '%_%';

-- Se crea una vista para analizar el tiempo de estimación de las entregas: 
create view tiempo_entrega AS
select o.order_id,
timestampdiff(DAY,o.order_estimated_delivery_date,o.order_delivered_customer_date) as diff_estimation
FROM orders as o;


