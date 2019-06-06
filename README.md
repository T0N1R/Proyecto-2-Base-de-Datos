# Proyecto No.3 - Base de Datos

El proyecto consiste en implementar una simulacion de puntos de venta centralizados para una coorporacion, aplicando conceptos de OLAP y DataWarehousing. Se realizo implementando distintos "puntos de venta" que puedan almacenar clientes, productos y ventas asi como una implementacion en Hadoop de un Data Warehouse que almacene la data para procesamiento y presentacion. 

## Inicio:
Al clonar el proyecto encontraras todas las fases del proyecto. La primera, consiste en el diseno de la base de datos. Para esto se genero un Dump de la base de datos de postgres, asi como un archivo .sql para la creacion de las tablas. La segunda fase se encuentra en la carpeta de "interfaz" donde se adjuntan las dos Interfaces. Una que implementa el agregar datos de una tienda a Postgres (proyectoB.py), el segundo que tambien agrega la data a MongoDB (proyectoC.py). La tercera parte consiste en la generacion de datos, esto se encuentra en el archivo cli.y que genera data para postgres y mongoDB segun requiera el usuario. Luego se implemento la base de datos en Hive, Hadoop. Esto para manejar el DataWarehouse, luego conectado con Tableau para manejar la reporteria de la fase de Inteligencia de negocios. Termina el proyecto con el envio de mensajes por Twitter, esto es una oferta que se genera para los tres clientes que mas compras generaron, Esto se encuentra en la carpeta de "twitter".

### Prerequisitos:
- Python 3.7
- Librerias varias de Python para la conexion a las bases de datos, graficos y twitter:
- - Twitter
- - PyQt5
- - psycopg2
- - pymongo
- mongoDB
- postgresql
- Hadoop
- - Hive

### Instalaciones
https://docs.mongodb.com/manual/installation/
https://www.postgresql.org/docs/9.3/tutorial-install.html
https://tecadmin.net/setup-hadoop-2-4-single-node-cluster-on-linux/
https://www.edureka.co/blog/apache-hive-installation-on-ubuntu

### Como correr los scripts:
Python Example:
```
pip install psycopg2
python3 proyectoC.py
```
