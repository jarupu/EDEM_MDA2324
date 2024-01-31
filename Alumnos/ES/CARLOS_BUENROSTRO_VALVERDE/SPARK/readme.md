# EL GRAN CIRCO DE LA FORMULA 1.

El presente Notebook pretende realizar un pequeño análisis en Spark para poder mostrar el potencial de dicha tecnología. En este caso se ha decidido hacer uso de diversos datasets (10 en total) basados en datos de la Formula 1 en los últimos 70 años. De esta forma, podremos utilizar joins entre tablas, filtrados, agrupados, orden en las tablas, renombramiento de columnas, entre otras funciones que nos permite Spark.

El índice de los ejercicios resueltos ha sido el siguiente:
1.  Cargar y mostrar todos los datasets empleados en el entregable.
2.  Conocer los pilotos y escuderías para las cuales han trabajado.
    1.  El último paso he sacado aquellas para las que ha corrido Fernando Alonso, aunque podría elegirse cualquier piloto que haya pasado por el Circo de la Formula 1.
3. Conocer el número de carreras comenzada por cada uno de los pilotos que han sido partícipes de la F1.
   1. Se ha realizado también un TOP 10 de los pilotos que más carreras han comenzado.
4. Conocer las escuderías que más puntos han obtenido a lo largo de su estancia en la F1.
   1. Se ha realizado un TOP 10 de las escuderías que más puntos han logrado.
5. Extraer la vuelta rápida por circuito, año y piloto en la clasificación.