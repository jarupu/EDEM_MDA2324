----PRIMERA SESIOON-----------------------------------------

--Ejercicio1: 
SELECT title, 
rental_rate,
replacement_cost,
ROUND (rental_rate/replacement_cost , 2) AS PORCENTAJE
FROM public.film;

--Ejercicio2: 

select 
	title,
	rental_rate,
	replacement_cost,
	ceiling(replacement_cost / rental_rate) as rent_time
from public.film;

-- Ejercicio3:

select
	count(title) as título,
	max(rental_rate) as precio_más_alto,
	min(rental_rate) as precio_más_bajo,
	avg(rental_rate) as precio_medio,
	stddev(rental_rate) as variabilidad_precios,
	min(replacement_cost) as reempalzo_más_bajo,
	max(replacement_cost) as reemplazo_más_alto
from public.film;


-- Ejercicio4:

select
	first_name
from public.actor
where first_name like 'A%';
select
	title
	from public.film
where rental_rate > 10;
select count (title)
from public.film
where rental_rate > 5 and rental_rate < 10;
select count (title)
from public.film
where rental_rate < 5 and length < 100;
select
	length
from public.film;

-- Ejercicio5:

SELECT avg(rental_rate)AS precio_medio
FROM public.film f;

-- Ejercicio6:

SELECT stddev(rental_rate)
FROM public.film f;

-- SEGUNDA SESIÓN------------------------------------

select title, rental_rate, replacement_cost from film;

select rating ,
count(distinct film_id) as total_peliculas,
avg(rental_rate) as precio_medio,
max(rental_rate) as mas_cara,
min(rental_rate) as mas_barata,
avg(length) as media_duracion,
min(extract(year from last_update)) as min_año,
max(extract(year from last_update)) as max_año
from film
group by rating;


SELECT rating, count(film_id) AS conteo_peliculas,
avg(rental_rate) AS precio_medio_alq,
avg(length) AS duración_media
FROM film
GROUP BY rating
HAVING count(film_id)>200 AND avg(film.rental_rate)>3 AND avg(length) >115

