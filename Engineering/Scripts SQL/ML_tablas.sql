use olist_pf;
-- Se crea una tabla para desarrollar un modelo de ML modelo 1

CREATE table ml_logistic_zip_table AS
SELECT 
    s.seller_zip_code_prefix,
    s.seller_city, 
    s.seller_state, 
    c.customer_zip_code_prefix,
    c.customer_city, 
    c.customer_state,
    p.product_weight_g,
    p.product_height_cm, 
    p.product_length_cm, 
    p.product_width_cm
        
FROM 
    order_items
    JOIN sellers AS s ON order_items.seller_id = s.seller_id
    JOIN products AS p ON order_items.product_id = p.product_id
    JOIN orders AS o ON order_items.order_id = o.order_id
    JOIN customers AS c ON o.customer_id = c.customer_id;
	
-- Se limpian los datos en base a los requerimientos de ML modelo1

DELETE FROM ml_logistic_zip_table WHERE product_weight_g IS NULL;

-- Se crea una tabla para que ML pueda trabajar en los datos, modelo 2

CREATE table ml_score_table AS
SELECT 
order_status,
oi.price as order_products_value,
oi.freight_value, 
order_purchase_timestamp,
order_approved_at,
order_estimated_delivery_date,
order_delivered_customer_date,
c.customer_state,
p.product_category_name,
p.product_name_lenght,
p.product_description_lenght,
p.product_photos_qty, 
r.review_score
        
FROM 
    orders
    JOIN customers AS c ON orders.customer_id = c.customer_id
    JOIN order_items as oi 	ON orders.order_id= oi.order_id
    JOIN products AS p ON oi.product_id = p.product_id
    JOIN order_reviews AS r ON orders.order_id = r.order_id;
    
-- limpieza de datos ML modelo 2
DELETE FROM ml_score_table as mt WHERE mt.customer_state IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.product_category_name IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.product_name_lenght  IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.product_description_lenght IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.product_photos_qty  IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.review_score  IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.order_delivered_customer_date IS NULL;
DELETE FROM ml_score_table as mt WHERE mt.order_approved_at IS NULL;

ALTER TABLE ml_score_table MODIFY COLUMN product_photos_qty INT;

