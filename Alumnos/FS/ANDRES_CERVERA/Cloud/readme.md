1. Creamos la primera instancia de maquina virtual(cloud-entregable)
2. Creamos el Bucket (cloud-entregable)

Como lo estamos haciendo sobre el mismo proyecto, no hace falta otorgar permisos de acceso

3. Creamos la instancia de Postgres (postgres)
4. Subimos el archivo create_statements.sql al bucket creado. Después lo importamos a la instancia de Postgres con el botón de importar. Por último desde la shell ejecutamos "gcloud sql connect postgres" y nos conectamos a la BD, donde al ejecutar "show tables; o \dt" visualizamos las tablas creadas.
5. Creamos los secretos username (postgres) y password (admin01)
6. Creamos la cloud function con las variables de entorno y secretos correspondientes (function-1)
7. Ahora con la función creada en cloud run, desplegamos una nueva revisión y le agregamos la instancia ya creada de postgres.
8. Navegamos hasta el dockerfile desde la shell y ejecutamos la imagen docker. Luego cambiamos el tag y la desplegamos.
9. Creamos el nuevo servicio en Cloud Run asociado a esa imagen.
10. Lanzamos el generador y cargamos la base de datos postgres.
11. Abrimos la URL de la imagen Grafana y visualizamos la interfaz. 
12. Nos conectamos a la BD y generamos dashboards con los datos de la BD (añadir /cloudsql/ delante del nombre de la conexión)