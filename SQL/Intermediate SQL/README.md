
#  Selecting Data :

- COUNT() : 
	- Counts only non-missing values
	- SELECT COUNT(birthdates) FROM people;
	- SELECT COUNT(DISTINCT birthdates) FROM people;
	- SELECT COUNT(birthdates), COUNT(users) FROM people;

	- Count total number of records in a table: SELECT COUNT(*) as total FROM people;


- ORDER OF EXECUTION : FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

- WRITTEN ORDER : SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT

---
#  Filtering Records :

- WHERE :
	- Filters individual records.
	- SELECT title FROM films WHERE release_year > 1960;
	- SELECT title FROM films WHERE name = "japan"	;
	- Except in a certain year <> NOT EQUAL TOs: 
		- SELECT title FROM films WHERE release_year <> 1960;
	
- OR, AND :
	- SELECT title FROM films WHERE name = "japan" AND country="EU";

- BETWEEN : Inclusive
	- SELECT title FROM films WHERE earnings BETWEEN 2 AND 5 AND country="UK";

- WILDCARDS :
	- Special characters used for pattern matching 
	- % matches 0, 1 or Many
	- _ matches single character

- LIKE :
	- SELECT title FROM films WHERE name LIKE 'S%';

- NOT LIKE :
	- SELECT title FROM films WHERE name NOT LIKE 'S%';

- IN :
	- SELECT title FROM films WHERE release_date IN (1930,2012,2025);

- IS NULL :

	- SELECT COUNT(*) FROM films WHERE name IS NULL;

- IS NOT NULL :

	- SELECT COUNT(name) FROM films WHERE birthdates IS NOT NULL;

--- 
#  Aggregate Functions : Summarizing Data

- AVG() :
	- SELECT AVG(budget) FROM films;

- SUM()

- MIN() : 
	- Can be used on non-numeric data.

- MAX()
	- Can be used on non-numeric data.	

- ROUND() :
	- SELECT ROUND(AVG(bugdet), 2) FROM films;


---

#  Sorting and Grouping

- ORDER BY : 
	- SELECT age FROM people ORDER BY age ASC/DESC;


- GROUPING : 
	- SELECT age, year FROM people GROUP BY age;

- FILTERING GROUP DATA :
	- HAVING : Filters grouped records.
































