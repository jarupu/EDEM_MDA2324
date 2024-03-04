# A continuación se describe el paso a paso en la creación del dashboard que muestra las  ventas del  Whole Foods Market en tiempo real:

Project 01
1. Creación de VM para las tiendas:

![Running ](./img/Imagen_1.png)

2. Creación de Bucket de donde tomaremos los mensajes.

![Running ](./img/Imagen_2.png)

3.	Creación de permisos en el project02:

![Running ](./img/Imagen_3.png)
![Running ](./img/Imagen_5.png)

4. Creación de tablas en SQL con las características necesarias:
![Running ](./img/Imagen_6.png)

5. Secrets y e ingreso de store_data_into_cloud_sql:

![Running ](./img/Imagen_7.png)
![Running ](./img/Imagen_8.png)

6.	Generación de repositorios en Artifact Registry: 

![Running ](./img/Imagen_9.png)
![Running ](./img/Imagen_10.png)

7.	Cloud Run: Creación de servicios:

![Running ](./img/Imagen_11.png)
![Running ](./img/Imagen_12.png)

8.	Generadores corriendo:

![Running ](./img/Imagen_13.png)
![Running ](./img/Imagen_14.png)

8.	Conexión a Grafana:

![Running ](./img/Imagen_15.png)