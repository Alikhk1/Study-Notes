
- **ORDER OF EXECUTION :** FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

- **WRITTEN ORDER :** SELECT -> FROM -> INNER JOIN -> ON/USING -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT


#  INNER JOIN : Only matching rows in both tables.


- ON:
	- SELECT p2.country, prime_minister, president
	  FROM presidents AS p1
	  INNER JOIN prime_ministers AS p2
	  ON p1.country = p2.country;

- USING:

	- SELECT p2.country, prime_minister, president
	  FROM presidents AS p1
	  INNER JOIN prime_ministers AS p2
	  USING (country);

- CONDITIONAL JOIN :

	- SELECT p2.country, prime_minister, president
	  FROM presidents AS p1
	  INNER JOIN prime_ministers AS p2
	  USING (country) AND p1.date = p2.date;

	
- table.column_name format must be used when selecting columns that exist in both tables.

---
#  JOINS ON JOINS : MULTIPLE JOINS

- SELECT *
  FROM left
  INNER JOIN right 
  ON left.id = right.id
  INNER JOIN another
  ON left.id = another.id AND left.date = right.date

---

#  OUTER JOINS: 

- LEFT JOINS:
	- Will return all records in the Left table and matching records in the Right table.
	- This is mostly used, instead of RIGHT JOINS.

- RIGHT JOINS:
	- Will return all records in the Right table and matching records in the Left table.

- FULL JOINS:
	- Joins Full Tables, some fields may have missing values.

---

#  CROSS JOINS:

- All Possible combinations of Two Tables.

---

#  SELF JOINS:

- Compare parts of the same table.
- Aliasing is required.

---

#  Set Operations: Do not require fields to join on. Number of Columns & Data Types should be Identical.

- UNIOIN:
	- UNION ALL : Duplicate records aswell.

	- SELECT *  
	  FROM left  
	  UNION  
	  SELECT *  
	  FROM right  

- INTERSECT: Returns only records appearing in both tables.

- EXCEPT: Records Unqiuely in left table.

---
#  Sub Querries:

- Query WHERE column IN (Sub Query)
- WHERE is most common place for Subquerries.
- They can be inside SELECT, FROM.

























