DROP DATABASE IF EXISTS olist_pf;
CREATE DATABASE IF NOT EXISTS olist_pf;
USE olist_pf;


/* Se crean primero las tablas que no dependen de las demás en relaciones (FK) para que no haya problemas
*/

# Tabla de marketing
DROP TABLE IF EXISTS marketing_qualified_leads;
CREATE TABLE IF NOT EXISTS marketing_qualified_leads (
    mql_id VARCHAR(60),
    first_contact_date DATETIME,
    landing_page_id VARCHAR(60),
    origin VARCHAR(60),
    PRIMARY KEY(mql_id)
);


# Tabla de productos
DROP TABLE IF EXISTS products;
CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(60),
    product_category_name VARCHAR(60),
    product_name_lenght DECIMAL,
    product_description_lenght DECIMAL,
    product_photos_qty DECIMAL,
    product_weight_g DECIMAL,
    product_length_cm DECIMAL,
    product_height_cm DECIMAL,
    product_width_cm DECIMAL,
    PRIMARY KEY(product_id)
);


# Tabla de traducción de productos
DROP TABLE IF EXISTS product_category_name_translation;
CREATE TABLE IF NOT EXISTS product_category_name_translation (
    product_category_name VARCHAR(60),
    product_category_name_english VARCHAR(60)
);


# Tabla de clientes
DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(60),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(60),
    customer_state VARCHAR(60),
    PRIMARY KEY (customer_id)
);


# Tabla de vendedores
DROP TABLE IF EXISTS sellers;
CREATE TABLE IF NOT EXISTS sellers (
    seller_id VARCHAR(60),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(60),
    seller_state VARCHAR(60),
    PRIMARY KEY(seller_id)
);


# Esta tabla de closed deals tiene datos numéricos para las últimas dos columnas
# pero hay muchos datos nulos por lo que los definimos como varchar
DROP TABLE IF EXISTS closed_deals;
CREATE TABLE IF NOT EXISTS closed_deals (
	closed_deals_id VARCHAR(60),
    mql_id VARCHAR(60),
    seller_id VARCHAR(60),
    sdr_id VARCHAR(60),
    sr_id VARCHAR(60),
    won_date DATETIME,
    business_segment VARCHAR(60),
    lead_type VARCHAR(60),
    lead_behaviour_profile VARCHAR(60),
	business_type VARCHAR(60),
    PRIMARY KEY (closed_deals_id),
    FOREIGN KEY (mql_id) REFERENCES marketing_qualified_leads(mql_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);


# Tabla de orders
DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(60),
    customer_id VARCHAR(60),
    order_status VARCHAR(60),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,
    PRIMARY KEY (order_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);


# Tabla de items de la orden
DROP TABLE IF EXISTS order_items;
CREATE TABLE IF NOT EXISTS order_items (
    order_id VARCHAR(60),
    order_item_id INT,
    product_id VARCHAR(60),
    seller_id VARCHAR(60),
    shipping_limit_date DATETIME,
    price DECIMAL,
    freight_value DECIMAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
    
);


# Tabla de pago de la orden
DROP TABLE IF EXISTS order_payments;
CREATE TABLE IF NOT EXISTS order_payments (
    order_id VARCHAR(60),
    payment_sequential INT,
    payment_type VARCHAR(30),
    payment_installments INT,
    payment_value DECIMAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);


# Tabla de reseñas de la orden
DROP TABLE IF EXISTS order_reviews;
CREATE TABLE IF NOT EXISTS order_reviews (
    review_id VARCHAR(60),
    order_id VARCHAR(60),
    review_score INT,
    review_comment_title VARCHAR(100),
    review_comment_message VARCHAR(255),
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
