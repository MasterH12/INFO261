/*Ejercicio 5.1*/
use sakila;
show tables;
describe film;
SELECT first_name ,last_name, city from customer as t1 inner join address as t2 on t1.address_id=t2.address_id inner join city as t3 on t2.city_id=t3.city_id;