-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id smallserial PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(30) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date char(10) NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id smallserial PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id smallserial REFERENCES employees(employee_id) NOT NULL,
	order_date char(10) NOT NULL,
	ship_city varchar(30) NOT NULL
);
