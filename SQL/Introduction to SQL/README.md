# Core Concepts

- Database: Organized collection of related data.

- Table: Structure within a database made of rows (records) and columns (fields).  
		- Table name should be lowercase with underscores.  
		- Field name should be lowercase, one word and singular.

- Primary Key: Unique identifier for each row.

- Foreign Key: Links data between tables.


---

#  Keywords :

- SELECT and FROM : 

	- SELECT field_name FROM table;

- ALIAS : as

	- SELECT name as First_Name FROM table;	

- DISTINCT : select only distinct values.

	- SELECT DISTINCT values FROM table;

- LIMIT : 

	- SELECT values FROM table LIMIT 2;

- TOP (SQL server) :

	- SELECT TOP(2) values FROM table;

---

#  VIEW : Saved SQL Query that acts like a virtual table.

- They don't data, they store the query.

- CREATE VIEW employee_hire AS SELECT name FROM table; (Then you can query it like a normal table). SELECT * from employee_hire

















