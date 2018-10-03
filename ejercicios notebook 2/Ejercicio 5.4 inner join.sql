/*Ejercicio 5.1*/
use sakila;
select title,count(title) from rental as t1 inner join inventory as t2 on t1.inventory_id=t2.inventory_id inner join film as t3 on t2.film_id=t3.film_id group by title;