
select @@version;

select @@datadir;

use sakila;

show databases;
-- database you are working right now 
select database();

show tables;

show columns from actor;

desc actor;

select * from performance_schema.users;

 --  statement query or access the data
 -- DDL, DML, DCL, TCL, DQL
 
select * from actor;

select actor_id, first_name from actor;
select first_name,actor_id from actor;

select first_name,actor_id, actor_id+5 from actor;

 -- where clause => conditon ( filter out the data)
 select first_name, actor_id
 from actor where actor_id>5;
 
select first_name
 from actor where actor_id>5;


select *
 from actor;


select first_name
 from actor where first_name<"E";
 
 
 
select first_name
 from actor where first_name>"E";
 
-- > ,< >=, <=, <>, !=

select first_name,actor_id
 from actor where actor_id!=5; 
 
 select * from actor;


select first_name,actor_id
 from actor where actor_id between 1 and 5;
 

select first_name,actor_id
 from actor where actor_id IN (2,4,6,8);

--  %, _
select first_name,actor_id
from actor where first_name like 'J%';

select * from actor;

select database();

create database if not exists sakila;

create database if not exists learning;

-- using it
use learning;

show tables;

--  create table name(col datatype)
create table product(product_id integer, product_name varchar(10));

show tables;

desc product;
--  insert the data ( DML)
insert into product(product_id, product_name) value("4",null),(5,"happy");

select * from product;
insert into product(product_id) value(6);

insert into product value(7,"jop");
select * from product;

insert into product value(7,"jop");
insert into product(product_name,product_id) value("kajal",8);

select * from product;

create table product2(product_id INT DEFAULT 7
, product_name varchar(10));

insert into product2(product_id, product_name) valueS(1,"MOBILE");
insert into product2(product_name) valueS("TV");
insert into product2(product_id, product_name) valueS(null,"MOBILE");
SELECT * FROM PRODUCT2;


drop table product3;
create table product3(product_id INT NOT NULL default 0 
, product_name varchar(10));

insert into product3(product_id, product_name) valueS(1,"MOBILE");
insert into product3(product_name) valueS("MOBILE");

select * from product3;

--  unique ( the value will be unique )
drop table product3;
create table product3(product_id INT unique default 0, product_name varchar(10));
insert into product3( product_id,product_name) valueS(0,"MOBILE2");
select * from product3;


-- new constraint ( PRIMARY KEY ( column should be unique and it shouldn't be null
drop table product3;

create table product3(product_id INT primary key default 0, 
product_name varchar(10));

insert into product3( product_id,product_name) valueS(null,"MOBILE2");
select * from product3;

desc product3;

drop table product3;
create table product3(product_id INT,
product_name varchar(10),
primary key(product_id)
);


-- new feature
create table product3(product_id INT auto_increment primary key,
product_name varchar(10));
insert into product3(product_name) valueS("MOBILE2");
insert into product3( product_id,product_name) valueS(10,"MOBILE2");

select * from product3;