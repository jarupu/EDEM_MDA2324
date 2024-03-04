select title, rental_rate, replacement_cost,
round(replacement_cost / rental_rate, 2) as ratio_alquiler_reemplazar
from public.film;

select title, rental_rate, replacement_cost,
ceil(replacement_cost / rental_rate) as break_even
from public.film;

select count(film_id) as pelicluas_disponibles,
max(rental_rate) as alquiler_max,
min(rental_rate) as alquiler_min,
avg(rental_rate) as alquiler_media,
stddev(rental_rate) as varibilidad,
min(replacement_cost) as remplazo_barato,
max(replacement_cost) as remplazo_caro
from public.film;

select *
from public.film
where title = 'Academy Dinosaur';

select title, rental_rate
from public.film
where rental_rate < 5;

select title
from public.film
where title in ('Titanic', 'Casablanca');

select title
from public.film
where title not in ('Titanic', 'Casablanca');

select first_name as nombre
from public.actor
where first_name like 'A%';

select title as titulo, rental_rate as precio_alquiler
from public.film
where rental_rate > 10;

select title as titulo, rental_rate as precio_alquiler
from public.film
where rental_rate between 5 and 10;

select title as titulo, rental_rate as precio_alquiler, length as duracion
from public.film
where rental_rate < 5 and length < 100;

select title as titulo, rental_rate as precio_alquiler
from public.film
where title in ('Giant Troopers', 'Gilbert Pelican', 'Gilmore Boiled');

select title as titulo, rating, length as duracion
from public.film
where title in ('Ali Forever');

select title as titulo, rental_rate as precio_alquilar
from public.film
where rental_rate = null;

select title as titulo, length as durasion
from public.film
order by length asc;

select title as top_5_mas_cortas, length as durasion
from public.film
order by length asc
limit 5;

select distinct rating, count(rating) as cantidad_peliculas,
round(avg(rental_rate), 2) as precio_medio_alquiler,
min(rental_rate) as alquiler_mas_barato,
max(rental_rate) as alquiler_mas_caro,
round(avg(length)) as duracion_media_peliculas
from public.film
group by rating;

select distinct rental_rate,
round(avg(length), 2) as duracion_media,
round(avg(replacement_cost), 2) as coste_reemplazo_medio
from public.film
group by rental_rate;

select distinct rating, 
count(rating) as cantidad_peliculas
from public.film
group by rating
having count(rating)>200;

select distinct rating,
round(avg(rental_rate), 2) as precio_medio_alquiler
from public.film
group by rating
having avg(rental_rate)>3;

select distinct rating,
round(avg(length), 2) as duracion_media
from public.film
group by rating
having avg(length)>115;

select distinct rating,
count(film_id) as numero_peliculas,
round(avg(rental_rate), 2) as precio_medio_alquiler,
min(rental_rate) as alquiler_min,
max(rental_rate) as alquiler_max,
round(avg(length), 2) as duracion_media,
min(year(release_year)) as pelicula_mas_antigua,
max(year(release_year)) as pelicula_mas_nueva
from public.film
group by rating;

select distinct rating as rating_mayor_200,
count(film_id) as numero_peliculas
from public.film
group by rating
having count(rating)>200;

select distinct rating,
round(avg(rental_rate), 2) as precio_medio_alquiler
from public.film
group by rating
having avg(rental_rate)>3;

select distinct rating,
round(avg(length), 2) as duracion_media
from public.film
group by rating
having avg(length)>115;

select first_name as nombre,
       address as direccion,
       city as ciudad,
       country as pais
from customer c
inner join address a on c.address_id = a.address_id
inner join city ct on ct.city_id = a.city_id
inner join country co on ct.country_id = co.country_id;

select distinct f.title as pelicula, first_name as actor, last_name as apellido
from film f
left join film_actor factor on f.film_id = factor.film_id
left join actor a on factor.actor_id = a.actor_id
where a.last_name like 'C%';

select distinct f.title as pelicula, count(a.actor_id) as reparto
from film f
left join film_actor factor on f.film_id = factor.film_id
left join actor a on factor.actor_id = a.actor_id
group by f.film_id;

select distinct f.title as pelicula, count(a.actor_id) as reparto
from film f
left join film_actor factor on f.film_id = factor.film_id
left join actor a on factor.actor_id = a.actor_id
group by f.film_id
having count(a.actor_id)>2;

select distinct f.title as pelicula, count(a.actor_id) as reparto
from film f
left join film_actor factor on f.film_id = factor.film_id
left join actor a on factor.actor_id = a.actor_id
group by f.film_id
order by count(a.actor_id) desc
limit 1;

create table if not exists public.reviews_pp(
	film_id int2 not null,
	customer_id int2 not null,
	review_date date not null,
	review_description varchar(100),
	constraint reviews_pkey primary key (film_id, customer_id)
);

insert into public.reviews_pp (film_id, customer_id, review_date, review_description)
values (4, 7, '02-28-2024' , 'Pocas peliculas me han parecido tan sosas como esta');

select *
from reviews_pp;

update public.reviews_pp
set review_description = 'De las peliculas mas interesantes de mi vida'
where customer_id = 7 and film_id = 4;

alter table reviews_pp
rename to reviews_pabloperez

delete
from public.reviews_pabloperez
where customer_id = 7;

drop table public.reviews_pabloperez

create view vista_pablo_perez as
select distinct rating,
count(rating) as numero_peliculas,
round(avg(rental_rate), 2) as alquiler_medio,
min(rental_rate) as precio_minimo,
max(rental_rate) as precio_maximo,
round(avg(length)) as media_minutes,
from public.film
group by rating
having count(*)>200;

select *
from vista_pablo_perez;

select actor_id, first_name, last_name, last_update
from public.actor
where first_name in (select first_name from
public.actor where last_name ilike 'C%')

select *
from film f
where language_id in (select language_id from
"language" l where l."name" = 'English')

select *
from customer c
where c.address_id in (select a.address_id from address a where a.address like 'A%');

select *
from customer c
where c.customer_id in (select p.customer_id from payment p where p.amount>'190');