CREATE TABLE bookInfo(
	id int(6) AUTO_INCREMENT NOT NULL,
	book_name varchar(120),
	book_isbn int(13),
	book_author varchar(80),
	book_price float(6),
	primary key (id)) default charset=utf8;