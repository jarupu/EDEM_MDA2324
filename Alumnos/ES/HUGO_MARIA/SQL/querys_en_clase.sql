-- Nueva Query

/* Ejercicio 1 */
select first_name as nombre, last_name as apellido
from actor a

/* Ejercicio 2*/
select title, rental_rate, replacement_cost, rental_rate  + replacement_cost as operacion,
concat(round(100 * rental_rate / replacement_cost, 2),'%') as rental_replacement /* The same as casting the numeric bit with ::varchar*/
from public.film


/*Ejercicio 3*/
select title, rental_rate, replacement_cost, ceil(replacement_cost / rental_rate)
from film f 

/*Ejercicio 4*/
select count(title) as Título 
from film f 

/*Ejercicio 5*/
select count(title) as titulos
	from film f 
/*Ejercicio 6*/
select title from film f 
where rental_rate > 4;

/*Ejercicio 7 - Todos los datos de la peli Academy Dinosaur*/
select * from film f 
where title = 'Academy Dinosaur'

/*Ejercicio 8 - Muestra todas las pelis que cuesten menos de 5€ de alquiler*/
select title, rental_rate from public.film 
where rental_rate <5

/*Ejercicio 9 - Actores que empiezan por la letra a*/
select first_name from actor a 
where first_name LIKE 'A%'

/*Ejercicio 10 - Pelis en alquiler por >4€*/
select title from film f 
where rental_rate > 4;

/* Ejercicio 11 - Pelis en alquiler entre 2€ y 4€*/
select title, rental_rate from film 
where rental_rate between 2 and 4

/*Ejercicio 12 - Cuántas pelis en alquiler por menos de 10€ y que duren menos de 100 min*/
select title, rental_rate, length from film 
where rental_rate < 5 and length < 100;

/*Ejercicio 13 - Precio de Giant Troopers, Gilbert Pelican y Gilmore Boiled*/
select title, rental_rate from film where title like 'Gi%';

/*Ejercicio 14 - rating y duración de Ali Forever*/
select title, rating, length from film where title like 'Ali Forever';

/*Ejercicio 15 - Pelis sin precio de alquiler*/
select count(title)  from film where rental_rate is null 

/*Ejercicio 16 - Responsable quiere conocer mejor sus pelis: listar pelis por oden de duración (- a +)
y conocer las 5 pelis más cortas*/
select title, length from film f 
order by length desc limit 5

/*Ejercicio 17 - Encuentra la peli más cara por minuto*/
select title, rental_rate, (rental_rate / length) as precio_minuto
from film order by precio_minuto desc limit 10

/*Ejercicio 18 - 10 pelis m´s antiguas cuyo precio de alquiler < 3€*/
select title, release_year, rental_rate
from film f 
where rental_rate < 3
order by release_year asc limit 10

/*Ejercicio 19 - Group by: selecciona pelis por rating: número de pelis*/
select rating, count(rating) as no_pelis, round(avg(rental_rate),2) as alquiler_medio, min(rental_rate) as alquiler_min,
max(rental_rate) as alquiler_max, round(avg(length), 2) as duración_media, 
min(release_year) as más_antigua, max(release_year) as más_reciente
from film f group by rating

/*Ejercicio 20 - HAVING - agrupar pelis por rating cuando haya más de X pelis en ese grupo*/
select rating, count(rating) as no_pelis, round(avg(rental_rate),2) as alquiler_medio, min(rental_rate) as alquiler_min,
max(rental_rate) as alquiler_max, round(avg(length), 2) as duración_media, 
min(release_year) as más_antigua, max(release_year) as más_reciente
from film f group by rating having count(rating) > 200