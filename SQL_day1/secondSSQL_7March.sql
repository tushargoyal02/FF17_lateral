use learning;


CREATE TABLE shirts (
    shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    article VARCHAR(50),
    color VARCHAR(50),
    shirt_size VARCHAR(5),
    last_worn INT
);

desc shirts;

INSERT INTO shirts (article, color, shirt_size, last_worn)  
VALUES 
	('t-shirt', 'white', 'S', 10),
	('t-shirt', 'green', 'S', 200),
	('polo shirt', 'black', 'M', 10),
	('tank top', 'blue', 'S', 50),
	('t-shirt', 'pink', 'S', 0),
	('polo shirt', 'red', 'M', 5),
	('tank top', 'white', 'S', 200),
	('tank top', 'blue', 'M', 15),
	('polo shirt','purple', 'M', 50);
    
select * from shirts;

select concat(article,' ' ,color) from shirts;

select concat_ws('$',article,null,shirt_size) from shirts;

select concat('hey',"hello");

select length("hello");

select length("漢字");

select char_length("漢字");


select substr("rajasthan",2,5);

select substr("rajasthan",-3,2);

select substring("rajasthan" from 2);
select substr("rajasthan" from 2);


select elt(5,"hey","hello");

select insert("Yamahao",3,4,"#");

--  instr return the index position  => instr(string, substring,starting, occurance)
select instr("rajasthan","a");

select locate("a","rajasthan",3);


select right("datauser",3);

select lpad(4545,3,0);
select rpad(4545,10,"#");


--  trim functions (trim some character or a white space from a string)

select trim(Leading from '     hey            user    ');
select trim(trailing from '     hey            user    ');
select trim(both from '     hey            user    ');

select trim(both 'x' from 'xxxfadsfsdahey  xxxx          userxxxxx');