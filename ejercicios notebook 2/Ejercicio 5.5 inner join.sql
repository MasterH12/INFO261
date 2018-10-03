/*Ejercicio 5.1*/
use sakila;
select title,max(suma) from (select title, sum(amount) as suma from film as t1 inner join inventory as t2  on t1.film_id=t2.film_id inner join rental as t3 inner join payment as t4 on t1.film_id=t2.film_id and t3.rental_id=t4.rental_id group by title) as alias;