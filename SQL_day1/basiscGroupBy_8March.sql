  use learning; 
   CREATE TABLE books 
    	(
    		book_id INT AUTO_INCREMENT,
    		title VARCHAR(100),
    		author_fname VARCHAR(100),
    		author_lname VARCHAR(100),
    		released_year INT,
    		stock_quantity INT,
    		pages INT,
    		PRIMARY KEY(book_id)
    	);
        
        
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES
    ('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
    ('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
    ('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
    ('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
    ('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
    ('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
    ('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
    ('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
    ('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
    ('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
    ('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
    ("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
    ('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
    ('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
    ('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
    ('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
    
--  limit  , fetch
select * from books limit 5,3;

-- sorting the data
select * from books order by pages desc;

select book_id, author_lname, stock_quantity from books 
order by stock_quantity, author_lname;

select book_id, author_lname, stock_quantity from books 
order by 3,2;
--  %
select book_id, book_id+10 as newbookId, author_lname from books 
order by author_lname desc;

desc books;

--  functions
select distinct author_fname from books;

select distinct(author_fname) from books;

select count(author_fname) from books;
select count(distinct(author_fname)) from books;

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES
    ('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, null);

select * from books;

select author_fname, count(released_year) from books
group by author_fname;

select * from books order by stock_quantity desc;

-- 
drop table test;
create table test(eid tinyint unsigned);

insert into test values(23.5545);
select * from test;


-- decimal data type
drop table test;
create table test(eid decimal(5,2));
insert into test values(258.126);
insert into test values(2589);

insert into test values(2589);
select * from test;


-- float , double
drop table test;
create table test(x float, y double);
insert into test values(12.23, 88.77);

insert into test values(12.232246546544654, 88.7754565465465);
select * from test;


-- boolean
drop table test;
create table test(x bool);
insert into test values(True);

select * from test;



-- date time data type
drop table userinfo;

create table userinfo( uid int, 
login date, loginTime time, userTime datetime);

-- date  YYYY-MM-DD
insert into userinfo values(1, '2022-02-20','11:00:00', '98-03-08');
select * from userinfo;

-- pseudo column
select  curdate();
select curtime();


select login, loginTime, month(login) from userinfo;
select login, loginTime, monthname(login) from userinfo;

select login, loginTime, year(login) from userinfo;


select login, loginTime, yearweek(login),yearweek(login,1), yearweek(login,2) from userinfo;

select login, loginTime, week(login) from userinfo;

select login, loginTime, weekofyear(login) from userinfo;
select login, loginTime, extract( year from login) from userinfo;


select login, loginTime, date_add( login, interval 1 Day) from userinfo;
select now();

insert into userinfo values(2,curdate(), curtime(), now() );
desc userinfo;

select current_timestamp();
--
use learning;
drop table userTiming;

create table userTiming( username varchar(20),
loginTime timestamp default current_timestamp,
timeUpdate timestamp on update current_timestamp );

insert into userTiming(username) values("tushar");
SET SQL_SAFE_UPDATES = 0;
-- update statement
update userTiming set username="Miles" where username="tushar";

select * from userTiming;

insert into userTiming(username,loginTime) values("tushar",'1971-02-01');
insert into userTiming(username,loginTime) values("tushar",'2037-02-01');


select loginTime, hour(loginTime) from userTiming;

-- case statement
select * from books;
/*
*/

select author_lname,released_year,
	case released_year when 2003 then "new century"
    end
    from books;

-- new one
select author_lname,released_year,
	case when released_year>=2003 then "new century"
    else "no data matched"
    end
    from books;
-- 
select author_lname,released_year,
	case when released_year between 1990 and 2000 then "Senior Citizen"
         when released_year between 2001 and 2010 then "Adult"
    else "Child"
    end as "newcol"
    from books;


select author_fname, author_lname,
	case
		when count(*)=1 then concat(count(*), ' ',"book")
        else concat(count(*), ' ',"book")
	end "Books Count"
from books where author_lname is not null
group by author_fname, author_lname;




select * from shirts;

use sakila;

show tables;
-- i need to get the payment_id and customer_id of those person 
-- where the amount is greater than the amount of payment id =1
select * from payment;
select amount from payment where payment_id=1;

select payment_id,customer_id,amount from payment
where amount>2.99;

select payment_id,customer_id,amount from payment
where amount> (select amount from payment where payment_id=1);

select round(avg(amount),2) from payment;

select payment_id,customer_id,amount from payment
where amount> (select round(avg(amount),2) from payment);

select customer_id, count(amount) 
from payment group by customer_id 
having count(amount) < (select count(amount) from payment where customer_id=1);

-- only 1 row  => single row subquery (< ,>, <=, >=, !=)
select customer_id, count(amount) as totalCount
from payment where customer_id>1 group by customer_id
having count(amount)<30
order by totalCount;

select amount from payment where customer_id=1;

-- multi row subquery ( IN ANY ALL, exits , nonexist)
select customer_id,payment_id,amount
from payment
where amount IN (select amount from payment where customer_id=61);

-- older one
select customer_id,payment_id,amount
from payment
where amount IN (4.99,0.99,5.99);


select customer_id, count(amount)
from payment group by customer_idl;



select customer_id,payment_id,amount
from payment
where amount >=ALL (select amount from payment where amount>0);

-- >ANY, < ANY, =ANY
-- > ANY  ( more than the minimum value of result set)
select amount*3 from payment where customer_id=61;

-- <ALL, >ALL 

select max(amount) from payment where amount>0;

select * from payment2;
drop table payment2;
create table customerOrder as select customer_id,amount from payment where customer_id between 2 and 4;

desc payment2;
desc payment;

select * from payment2;

select customer_id, max(amount) from payment
group by customer_id;


select customer_id,amount 
from payment2 where exists(select customer_id, max(amount) from payment
group by customer_id);

select customer_id, max(amount) from payment
group by customer_id;


insert into 


select customer_id,amount
from payment2 where  exists(select customer_id from payment);

select * from customerOrder;
insert into customerOrder values(121,77.77);


-- CRreate, retrieve, 
-- update, delete, drop, truncate, alter
use sakila;
select * from customerOrder




update customerOrder set amount=99,customer_id=199 where customer_id=4;

-- dml
delete from customerOrder where customer_id=1;
drop table customerOrder;
create table customerOrder  as select * from payment;

select * from customerOrder;
-- end the transaction
truncate customerOrder;

drop table customerOrder;


create table test2(id int primary key);

insert into test2 values(10);
desc test2;
delete from test2;

truncate test2;


desc test2;
alter table test2
add column fname varchar(20);

alter table test2
rename column fname to FullName;

alter table test2
change column FullName newName char(20);

select * from test2;

insert into test2 values(3,"tushar2",1011);




