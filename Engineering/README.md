# <h1 align=center>***Data Engineering***</h1>

## **TABLA DE CONTENIDO**  
+ [1- Introducción.](#introducción) 
+ [2- Objetivos de trabajo.](#objetivos-de-trabajo)
+ [3- Tecnologías.](#tecnologías)
+ [4- Diagrama EDR.](#diagrama-edr)
+ [5- Flujo de datos.](#flujo-de-datos)
 
 
<hr>

# ***Introducción***

Esta parte del proyecto se encarga de las áreas que involucran al data engineering, tenemos el desafío de crear un Data Warehouse completamente funcional que sea accesible tanto para el área de Analitycs como para el área de Machine Learning. Además, debemos tener nuestra base de datos en AWS e implementar Airflow. 


<hr>  

# ***Objetivos de trabajo***  

Como objetivos en esta instancia nos planteamos:

- La construcción de una base de datos montada en AWS mediante el servicio RDS.
- Un pipeline que maneje el flujo de los datos, tanto su extracción, como limpieza y carga a la base de datos.
- La implementación de Airflow como orquestador de flujo de datos para automatizar los procesos.

<hr>  

# ***Tecnologías***  

- AWS (RDS y EC2)  
- Python  
- Pandas  
- MySQL  
- Airflow 

**AWS** en los dos servicios utilizados, funcionan como hosting, prestando recursos para poder almacenar la información y encargarse de proporcionar la capacidad de cómputo necesaria para brindar un servicio constante para la base de datos y para airflow.

**RDS** es un servicio que se encarga de proporcionarnos una base de datos relacional con el motor de MySQL, y **EC2** por su parte, nos provee de un sistema maleable en el que montamos una imagen de Linux, donde instalamos Airflow y demás dependencias necesarias para la automatización.

**Python** y **pandas** se encargan de, mediante scripts, construir la estructura y aplicar los cambios necesarios para la extracción, limpieza y carga de los datos. [Informe de ETL](https://www.notion.so/Informe-ETL-9190fc70e4d9405492c799a27b06418d)

**MySQL** es en donde va a estar creado nuestro Data Warehouse y desde allí nos encargamos de realizar tareas de mantenimiento que se hayan pasado por alto en algún proceso de limpieza, y también de generar las tablas necesarias para que tanto el área de Analytics como de ML, puedan alimentarse correctamente.

**Airflow** se encarga de la automatización del proceso de ETL que mediante el uso de DAGs, agenda tareas a ejecutarse de manera automática.


<hr>  

# ***Diagrama EDR***

Contamos con 2 tablas de hecho y 7 tablas de dimensión principales, más algunas tablas auxiliares que nos ayudan a que nuestra base de datos esté completa. Las tablas de hecho se corresponden con cada uno de los grupos de clientes para los que está propuesto el proyecto. La primer tabla de hecho `closed_deals` corresponde con los tratos cerrados por Olist y sus vendedores, y por otra parte la tabla `orders` representa las ventas de cada uno de los vendedores.


<img src="https://i.imgur.com/Ql5tnO3.png"  height=400 align="center">


# ***Flujo de datos***
<img src="https://i.imgur.com/usUJ4O8.png"  width=650>

El flujo de los datos ideal que planteamos en este caso es:

* Los datos son extraídos de una API provista por la empresa.
* Se limpian los datos mediante un script y se guardan limpios.
* Otro script toma los datos limpios y los carga a su respectiva tabla en la base de datos, dependiendo del nombre del archivo.
* La base de datos sirve para alimentar a los modelos de ML y los reportes y dashboards en PowerBI.

