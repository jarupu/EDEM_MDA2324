## Explicación Ejercicio

Para poder realizar este trabajo he utilizado un archivo .txt, el cual es el libro de "El Código Da Vinci".

Creamos y ejecutamos el docker-compose.

Creamos un topic en Confluent y lo configuramos para poder enviar/recibir los datos procedentes del producer. Ejecutamos el producer
y el consumer, de esta manera podremos ver los mensajes que se producen en el topic (cada mensaje es una línea del libro).


Corremos el segundo producer (producer2.py).

Cuando tenemos todo esto en funcionamiento levantamos el contenedor de docker que necesitamos en este momento, el cual nos permite procesar los datos mediante KSQL.

Creamos un topic ("palabras" en mi caso) y realizamos las búsquedas que deseemos en KSQL, en este ejercicio hacemos una búsqueda para que nos devuelva las palabras que empiezan por la letra 'r'.