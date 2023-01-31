# Se ajustan las ciudades a "sao paulo" en una lista de ciudades con diferente formato

UPDATE sellers
SET seller_city = "sao paulo"
WHERE seller_city IN ("sao paluo", "sao  paulo", "sao paulo - sp",
"sao paulo / sao paulo", "sao paulo sp", "sao paulop", "são paulo", "sp", "sp / sp", "sao pauo")
AND seller_state = "SP";

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