use olist_pf;


CREATE VIEW analytics_score AS
SELECT 
    avg(r.review_score),
    oi.seller_id
FROM 
    order_items as oi
    JOIN order_reviews AS r ON r.order_id = oi.order_id
GROUP BY oi.seller_id;

CREATE VIEW analytics_score_2 AS
SELECT 
    round(avg(r.review_score)),
    oi.seller_id
FROM 
    order_items as oi
    JOIN order_reviews AS r ON r.order_id = oi.order_id
GROUP BY oi.seller_id;

CREATE VIEW analytics_seller_reviews AS
SELECT 
    r.review_score,
    r.review_comment_title,
    r.review_comment_message, 
    oi.seller_id
FROM 
    order_items as oi
    JOIN order_reviews AS r ON r.order_id = oi.order_id;
    
    CREATE table analytics_seller_reviews AS
SELECT 
    r.review_score,
    r.review_comment_title,
    r.review_comment_message, 
    oi.seller_id
FROM 
    order_items as oi
    JOIN order_reviews AS r ON r.order_id = oi.order_id;
    
    
    CREATE table analytics_inflacion_order AS
SELECT 
    oi.order_id,
    oi.order_item_id,
    oi.product_id,
    oi.seller_id,
    oi.shipping_limit_date,
    oi.price,
    oi.freight_value,
    o.order_purchase_timestamp
FROM 
    order_items as oi
    JOIN orders AS o ON o.order_id = oi.order_id;

ALTER TABLE analytics_inflacion_order
ADD COLUMN price_cor_inflacion DECIMAL(10,2) NOT NULL;

ALTER TABLE analytics_inflacion_order
ADD COLUMN freight_cor_inflacion DECIMAL(10,2) NOT NULL;


UPDATE analytics_inflacion_order
SET price_cor_inflacion = round((price/(1+0.0629)),2)
WHERE order_purchase_timestamp BETWEEN '2016-09-04 21:15:19' AND '2016-12-23 23:16:47';

UPDATE analytics_inflacion_order
SET price_cor_inflacion = round((price /(1+0.0295)),2)
WHERE order_purchase_timestamp BETWEEN '2017-01-05 11:56:06' AND '2017-12-31 23:29:31';

UPDATE analytics_inflacion_order
SET price_cor_inflacion = round((price / (1 + 0.0375)),2)
WHERE order_purchase_timestamp BETWEEN '2018-01-01 02:48:41' AND '2018-08-24 11:44:39';

UPDATE analytics_inflacion_order
SET freight_cor_inflacion = round((freight_value/(1+0.0629)),2)
WHERE order_purchase_timestamp BETWEEN '2016-09-04 21:15:19' AND '2016-12-23 23:16:47';

UPDATE analytics_inflacion_order
SET freight_cor_inflacion = round((freight_value /(1+0.0295)),2)
WHERE order_purchase_timestamp BETWEEN '2017-01-05 11:56:06' AND '2017-12-31 23:29:31';

UPDATE analytics_inflacion_order
SET freight_cor_inflacion = round((freight_value / (1 + 0.0375)),2)
WHERE order_purchase_timestamp BETWEEN '2018-01-01 02:48:41' AND '2018-08-24 11:44:39';


