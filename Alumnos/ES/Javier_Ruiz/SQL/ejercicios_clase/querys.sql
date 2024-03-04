select title, rental_rate, replacement_cost, rental_rate + replacement_cost as suma
from film f 

select avg(rental_duration)
from film f 

select title, rental_rate, replacement_cost, concat(round(rental_rate / replacement_cost * 100, 2)::varchar , '%') as porcentaje
from film f 

select title, rental_rate, replacement_cost, ceil(replacement_cost / rental_rate) as umbral_rentable
from film f 

select * 
from film f
where title = 'Academy Dinosaur';


select * 
from film f
where rental_rate < 5;

select *  
from actor
where first_name ilike 'A%';

select * 
from film f
where rental_rate > 4;

select *
from film f
where rental_rate between 2 and 5;

select * 
from film f
where rental_rate < 5 and length < 100;

select title, rental_rate
from film f
where title like 'Gi%' ;

select title, rating, length
from film f 
where title like 'Ali Forever';

select title, rental_rate
from film f 
where rental_rate is null ;

select title, length
from film f
order by length ASC
limit 5;

select title, rental_rate, length, rental_rate / length as price_per_minute
from film f
order by price_per_minute DESC
limit 1;

select title, release_year, rental_rate
from film f
where rental_rate <3
order by release_year asc;


select rating, count(*) as count,
round(avg(rental_rate),2) as avgrate,
round(min(rental_rate),2) as minrate,
round(max(rental_rate),2) as maxrate,
round(avg(length),2) as avglenght,
max(release_year) as maxyear,
min(release_year) as minyear
from film f
where length > 55
group by rating, release_year
having count(title) > 200 and avg(rental_rate) > 3

select rating, count(title)
from film
group by rating
having count(title) > 200

select rating, avg(rental_rate)
from film f
group by rating 
having avg(rental_rate) between 1 and 3;

select rating, avg(length)
from film f
group by rating
having avg(length) between 115 and 200;

select rating::varchar
from film f
group by rating
having rating::varchar like 'P%';

select c.address_id, c.first_name, c.last_name, a.address, city.city, pais.country
from customer c
left join address a on c.address_id = a.address_id
left join city city on a.city_id = city.city_id 
left join country pais on city.country_id = pais.country_id

select p.country, count(c.customer_id)
from country p
left join city ci on p.country_id = ci.country_id
left join address a on ci.city_id = a.city_id 
left join customer c on c.address_id = a.address_id 
group by p.country

select f.title, a.first_name, a.last_name
from film f
inner join film_actor fa on fa.film_id = f.film_id 
inner join actor a on fa.actor_id = a.actor_id 
where a.first_name like 'C%'

select f.title, count(fa.actor_id)
from film f
inner join film_actor fa on fa.film_id = f.film_id 
group by f.title

select f.title, count(fa.actor_id)
from film f
inner join film_actor fa on fa.film_id = f.film_id 
group by f.title
having count(fa.actor_id) > 2

select f.title, count(fa.actor_id)
from film f
inner join film_actor fa on fa.film_id = f.film_id 
group by 1
order by 2 desc limit 1

create table if not exists review_jarupu(
film_id int2 not null,
customer_id int2 not null,
review_date date not null,
review_description varchar(50) not null,
constraint review_jarupu_pkey primary key (film_id, customer_id),
constraint film_jaruactor_id_key foreign key (film_id) references public.film(film_id) on delete restrict on update cascade, 
constraint customer_jaru_id_key foreign key (customer_id) references public.customer(customer_id) on delete restrict on update cascade
);

insert into reviews_jorgeredbull (film_id, customer_id, review_description) values ('07', '33', 'Jorje')

insert into reviews_tonifaura (film_id, customer_id, review_date, review_description) values ('22', '04','2080-07-11','Yeee k pasa prim')

select * 
from review_jarupu

insert into review_jmp (film_id, customer_id, review_date, descripcion_reseña) values ('22', '04','2080-07-11','control + foakkk')

update review_jarupu 
set review_date = '2000-10-17'
where customer_id = 2

alter table reviews_jorgeredbull
drop column review_date;

alter table reviews_reyes 
rename column review_description
to mi_fakin_opinion

create view jarupu_ferrari as
select c.address_id, c.first_name, c.last_name, a.address, city.city, pais.country
from customer c
left join address a on c.address_id = a.address_id
left join city city on a.city_id = city.city_id 
left join country pais on city.country_id = pais.country_id;

select f.title
from film f
where f.language_id in (select l.language_id from language l
where l.name = 'English')

select c.first_name, c.last_name
from customer as c
where c.address_id  in (select a.address_id
from address a
where a.address like '1%')

select c.first_name, c.last_name
from customer as c
where c.customer_id in (select p.customer_id
from payment p
group by p.customer_id
having sum(p.amount) > 190)

with subquery1 as (
select p.customer_id, sum(p.amount) as total_amount
from payment p
group by 1
having sum(p.amount) > 190)
select sum(total_amount), count(customer_id)
from subquery1

--numero de veces que un cliente ha alquilado una pelicula
with subquery2 as (
    select cu.customer_id, f.film_id, f.title, count(rt.rental_id) as counta
    from customer cu
    join rental rt ON cu.customer_id = rt.customer_id
    join inventory inv ON rt.inventory_id = inv.inventory_id
    join film f ON inv.film_id = f.film_id
    group by cu.customer_id, f.film_id, f.title
)
select cu.first_name, cu.last_name, nv.title, nv.counta
from  numveces nv
join  customer cu on nv.customer_id = cu.customer_id
order by nv.counta desc



