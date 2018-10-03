/*Ejercicio 5.1*/
use sakila;
show tables;
describe film;
SELECT first_name ,last_name from customer as t1 inner join film as t2 on t2.title='CHICAGO NORTH';