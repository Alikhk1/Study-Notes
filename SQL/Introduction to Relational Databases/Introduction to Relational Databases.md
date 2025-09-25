
- Relational Database Models real life entities by storing them in interconnected tables.
- They reduce redundancy (data only shows up one time)
- Enforce data integrity by relationships
- The idea of a database is to push data into a certain structure, a pre-define model, where you enforce data types, relationships and other rules.

- Information schema is meta databases that holds information about your current database. Holds various information in various tables.

- ERD : Squares denote entity types while circles are attributes or columns


-Integrity Constraints : Consistency, Quality, Structure.

	1. Attribute Constraints : DataTypes for each column

	2. Key Constraints : Enforced through primary key (each record is uniquely identified in a table)
		- Primary Key : Unique, Not Null, Time Invariant.
		- Superkey : Combination of All Attributes.
		- Minimal Superkey : No Attributes can be removed w/o losing the uniqueness property.
		- Candidate keys : Minimal Superkeys which can be chosen as the primary key.
		- Surrogate Key : An artificial key created to uniquely identify a row, with no real-world meaning.
		- HOW TO IDENTIFY KEYS IN A TABLE :
			- SELECT COUNT(DISTINCT(<column_names)) 
			  FROM <table_name>;
			- If resulting number equals the total rows in table, the combination or column can uniquely identify them.

	3. Referential Integrity Contraints : A record referencing another table must refer to an existing record in that table. Enforced through Foreign keys which 					      glue tables togather.
		- Duplicates & Null values are allowed.
		- MANY TO MANY : Relational databases cannot directly model many-to-many.You create a junction (bridge) table that breaks it into two 1 to Many.
			CREATE TABLE student_courses (
			  student_id INT,
			  course_id INT,
			  PRIMARY KEY(student_id, course_id),
			  FOREIGN KEY (student_id) REFERENCES students(id),
			  FOREIGN KEY (course_id) REFERENCES courses(id)
			);
			


- Type Casting : CAST ( <column_name> AS integer )

--- 

#  Table Creation, Insertion, Modification :
,
- CREATE TABLE <name> (
>	<column#1_name> \<DataType>,  
	<column#2_name> \<DataType>  
  );

- ADD A NEW COLUMN :
	
>	ALTER TABLE \<table_name>  
	ADD COLUMN \<column_name> \<DataType>;

- CHANGE COLUMN NAME : 

>	ALTER TABLE \<name>  
	RENAME COLUMN \<old_name> TO \<new_name>;

- DELETE COLUMN : 

>	ALTER TABLE \<table_name>  
	DROP COLUMN \<column_name>;

- COPYING DATA FROM ONE TABLE TO ANOTHER :

>	INTERT INTO \<table_name>  
>	SELECT DISTINCT \<column_name(s)>  
>	FROM \<table_name>;  

- INSERT VALUES MANUALLY INTO A TABLE :
	
>	INTERT INTO <table_name> (column#1, column#2)  
	VALUES ("value#1", "value#2")

- CHANGE DATA TYPE OF A COLUMN : 
	
>	ALTER TABLE \<table_name>  
>	ALTER COLUMN \<column_name>  
>	TYPE \<DataType>;    

- SET OR REMOVE NON NULL :

>	ALTER TABLE \<table_name>  
	ALTER COLUMN \<column_name>  
	SET NOT NULL / DROP NOT NULL;

- ADDING CONSTRAINTS :

>	ALTER TABLE <table_name>  
	ADD CONSTRAINT some_name UNIQUE/PRIMARY KEY (column_name);

- PRIMARY KEY : 

>	CREATE TABLE \<table_name> (
		\<column_name> \<DataType> PRIMARY KEY;  
	);

OR:
	
> CREATE TABLE \<table_name> (  
		a interger,  
		b integer,  
		c integer,  
		PRIMARY KEY (a,b)  
	);
	
- SURROGATE KEY FROM EXISTING COLUMNS :

>	ALTER TABLE \<table_name>  
	ADD COLUMN \<column_name>;  
>   UPDATE \<table_name>
> 	SET \<column_name>  = CONCAT(\<column_a>, \<column_b>);  
	ALTER TABLE \<table_name>  
	ADD CONSTRAINT some_name PRIMARY KEY \<column_name>;

- FOREIGN KEY : 

>	CREATE TABLE \<table_name#1> (
		\<column_name> \<DataType> REFERENCES \<table_name#2> (\<column_name>)
	);

OR:
	
>	ALTER TABLE <table_name#1>  
	ADD CONSTRAINT some_name FOREIGN KEY (\<name>) REFERENCES \<table_name#2> (\<column_name>);











