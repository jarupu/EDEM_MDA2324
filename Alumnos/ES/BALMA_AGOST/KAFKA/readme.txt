POSTWORK

Para realizar este trabajo he utilizado un fichero txt (KAFKA\libro.txt) de un libro, en este caso concreto, El Código Da Vinci.

El primer paso es inicializar el consumidor y el productor. 

Luego es necesario que creemos el tema y lo a configuraremos para que sea capaz de enviar/recibir los datos producidos.Los datos que se envían por consola son cada una de las líneas que encontramos dentro del fichero txt.

El siguiente paso es levantar el contenedor Docker para que sea capaz de procesar los datos a través de KSQL y realizar las consultas pertinentes a través de un topic, en este caso, topic_postwork.
