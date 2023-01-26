<h1 align=center> Machine Learning </h1>

## Índice:

+ [1- Introducción.](#introducción)
+ [2- Objetivos.](#objetivos)
+ [3- Explicación de los modelos.](#explicación-de-los-modelos)
+ [4- Aclaraciones.](#aclaraciones)
+ [5- Conclusiones.](#conclusiones)

## Introducción:

Desde el área de Machine Learning de AllemBI planteamos dos aplicaciones para nuestro portal web con la finalidad de servir como herramienta tanto para los vendedores que publican sus productos en Olist, como para la misma empresa; y para desarrollarlas implementamos dos modelos de aprendizaje automático que se alimentan de los datos que residen en nuestro DataWarehouse hosteado en AWS por el sector de Engineering.

## Objetivos:

¿Qué hace que un comprador califique de forma negativa a un producto luego de comprarlo? ¿Podemos predecir con exactitud la calificación que nos dará un comprador antes de realizar la orden?

Bueno, con el fin de responder estas preguntas pensamos en analizar los datos para encontrar alguna correlación entre la calificación (Que puede ir de 1 a 5 estrellas) y características tales como el precio del producto, el tiempo de envío y demás. Luego, con la ayuda de un `modelo de regresión` como lo es `Random Forest` y algunas transformaciones de datos, buscamos predecir este valor para poder crear una aplicación dentro de nuestro portal web que ayude a los vendedores a saber si recibiran un buen feedback o si deberían plantearse alguna modificación en la publicación del producto.

Por otro lado, además de ayudar a los vendedores de Olist, nos gustaría entregarle al sector de logística de Olist una herramienta que permita determinar el mejor método de envío para un pedido según tamaño, peso y puntos de partida y llegada, con esto no solo buscamos una mejora a nivel económico reduciendo gastos innecesarios de transporte, sino que también ayudaríamos a reducir la huella de carbono, ya que, por ejemplo, si un paquete es pequeño, ligero y el envío se hace entre dos puntos cercanos, podríamos utilizar un transporte más barato y sano como una bicicleta o una moto en lugar de usar un vehículo como un auto o una camioneta. Para conseguir esto, instanciamos un `modelo de clusterización` como lo es `K-means` para agrupar nuestros productos en 3 grupos y, junto con algunas reglas que implementaremos, determinar el mejor método de envío.

## Explicación de los modelos:

<h1 align=center> Random Forest </h1>

Utilizaremos un modelo de Regresión Random Forest para intentar predecir el review_score que obtendrá una orden basandonos en el conjunto de features analizados. La lógica detrás de este modelo es construir varios árboles de decisión y combinarlos para obtener una mejor precisión en la predicción. Cada árbol de decisión se construye a partir de un subconjunto aleatorio de características y un subconjunto aleatorio de muestras de entrenamiento. Al combinar varios árboles de decisión, se obtiene una mejor precisión debido a que los errores individuales de cada árbol se promedian y se reduce la varianza en las predicciones. Algo a tener en cuenta, es que inicialmente notamos que no había una fuerte correlación en nuestros datos, por lo que decidimos agregar nuevas features calculadas apartir de otras columnas, tales como:

+ Tiempo estimado de entrega en días hábiles: 'tiempo_envio_estimado'
Un comprador puede estar poco satisfecho si el tiempo estimado de entrega es alto.

+ Tiempo real de entrega en días hábiles: 'tiempo_envio_real'
Un comprador puede estar más satisfecho si su producto llega antes de lo esperado.

+ Delta de tiempo de entrega en días hábiles: 'delta_tiempo_envio'
Diferencia entre la fecha estimada y la fecha real del envío, si este valor es negativo la entrega se hizo antes del tiempo estimado, si es positivo, el envío tardó más de lo estimado.

+ Entrega tardía: 'entrega_tardia'
False si el pedido llegó antes de tiempo, True si el pedido se atrasó al tiempo estimado.

+ Precio total del pedido: 'precio_total'
Un comprador puede estar más o menos satisfecho según el precio total de su pedido.

+ Relación precio envio/producto: 'relacion_envio_producto'
Un comprador puede esperar un mejor servicio logístico si el precio del producto es alto.

<h1 align=center> K-Means </h1>

Utilizaremos un modelo de clusterización K-Means con el objetivo de agrupar los productos por tamaño, en 'Chico', 'Mediano' o 'Grande' según nuestros datos de dimensiones (height, lenght y width). Esto, junto con algunas reglas que implementaremos, nos ayudará a determinar un método de envío óptimo para el pedido entre nuestras cuatro opciones, 'Bicicleta', 'Moto', 'Camioneta' y 'Camión'. Las reglas que se tuvieron en cuenta para elegir el método de envío son:

+ Bicicleta 🚲: El producto debe ser 'Chico', no debe pesar más de 8kg y el envío debe ser dentro de la misma zona (Mismo zip_code para seller y customer).

+ Moto 🛵: El producto debe ser 'Chico' o 'Mediano', no debe pesar más de 15kg y el envío debe ser dentro de la misma ciudad sin importar zip_code.

+ Camioneta 🚍: El producto puede ser 'Chico', 'Mediano' o 'Grande, no debe pesar más de 75kg y el envío debe ser dentro del mismo estado, sin importar ciudad.

+ Camión 🚚: El producto puede ser 'Chico', 'Mediano' o 'Grande' y el envío debe ser entre distintos estados.

### Disclaimer: 

Como sabemos, K-Means es un algoritmo de agrupamiento no supervisado, ideal para nuestro caso en el que no tenemos datos sobre el método de envío, sin embargo, si queremos que nuestros resultados sean aplicables a la realidad, debemos inferir en los mismos mínimamente para así conseguir datos de calidad que sirvan para buscar implementar soluciones a la problemática planteada, por ello, si bien el modelo se instanció desde un principio con 5 clusters, fusionaremos algunos de estos clusters para dividir nuestros datos en 3 grupos en lugar de 5, y así obtener la distribución deseada.

¿Y por qué no instanciar el modelo con 3 clusters desde un inicio? Simplemente porque, al dividir la totalidad de nuestros datos en únicamente 3 grupos, el modelo busca patrones más generales que hacen que las distribuciones varíen y que obtengamos resultados ilógicos como por ejemplo, que un paquete cuyas dimensiones son de 10cm x 10cm x 10cm debería pertenecer al grupo de productos 'Grande' y que uno de dimensiones 200cm x 15cm x 20 cm pertenece al grupo 'Chico'.

## Aclaraciones:

Hay tres puntos a remarcar:

+ 1.- Este readme cumple la función de introducirnos de forma resumida a la problemática planteada y a las soluciones que encontramos, de ningún modo es un informe detallado sobre el instanciamiento de los modelos, para ello, los invitamos a revisar los Notebooks.ipynb en los cuales encontrarán información paso a paso sobre las transformaciones realizadas, las decisiones tomadas y la creación de los modelos.

+ 2.- Si bien los Notebooks.ipynb correspondientes a cada modelo contienen información detallada sobre el proceso de creación de los mismos, cabe destacar que dichos informes se encuentran levemente resumidos y preparados para su presentación, con esto me refiero a que se decidió con antelación la selección de features sabiendo el modelo que queríamos plantear y los datos que ibamos a necesitar luego de varias pruebas, ninguna decisión fue tomada de forma aleatoria, solo que para que el informe sea más claro y limpio, los modelos se encuentran en su versión final con una pequeña excepción que comentaremos en el siguiente punto.

+ 3.- A la hora de hacer nuestra aplicación para determinar el método de envío óptimo, intentamos aplicar un modelo de clasificación como lo es el Árbol de Decisión, con el fin de realizar toda la aplicación mediante modelos de Machine Learning, esta idea se descartó principalmente debido al enorme desbalanceo que hay en nuestros datos, ya que afectaba de forma muy negativa a nuestros resultados, sin embargo, todo el análisis se mantuvo al final del reporte para que se pueda ver el proceso y también en caso de que se retome la idea aplicando alguna solución.

## Conclusiones:

+ Es posible predecir el review_score que tendrá una orden utilizando un modelo de Regresión y si bien no hay demasiadas correlaciones fuertes incluso luego de implementar nuevas features, es evidente que uno de los puntos que influye en la calificación es el tiempo de envío de la orden, con esta información, los vendedores pueden optar por otras opciones a la hora de entregar el pedido, como por ejemplo, proponerle al comprador que retire su producto por el local en caso de ser posible.

+ Si queremos hacer una aplicación para determinar el método de envío óptimo podemos apoyarnos de un modelo de clusterización para agrupar nuestros productos por tamaño, aunque al ser éste un modelo no supervisado con las limitaciones y problemáticas que significa, lo recomendable es continuar el proceso de forma supervisada almenos para el resto de parámetros, y así, crear una aplicación que nos otorgue resultados de calidad.
