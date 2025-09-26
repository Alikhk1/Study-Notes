
- SnowSight : SnowFlake web interface.
---
#  DataTypes & Conversions

1. NUMBER (p, s): Precision & Scale. Maximum = 38.

2. TIMESTAMP_LTZ : DATE + TIME  YYYY-MM-DD HH-MM-SS

3. CAST (\<Source_Column> AS \<Target_DataType>), \<Source> :: \<DataType>

4. TO_VARCHAR ( \<exp> )

5. TO_DATE ( \<exp> )

6. DESC TABLE \<table_name> : Get Information on all columns in a table with their DataTypes

---

#  Functions, Sort, Grouping :

1. INITCAP (\<exp>) : Capitalizes Each word in a String.

2. CONCAT (\<exp>, \<exp>) 

3. CURRENT_DATE/TIME

4. EXTRACT (\<date/time> FROM \<date/time>)

5. GROUP BY ALL : Automatically group by all columns in SELECT.

---
#  Joining :

1. Natural Joins : Automatically Join & Eliminate Duplicate Columns.

2. Lateral Joins : For every row in the left table, execute the subquery on the right, where the subquery can reference columns from that row.
		   We need to alias after Lateral or we get error.


---

#  SubQuerries & Common Table Expressions :

1. Uncorrelated Subquery :  Subquery is unrelated to the outter query.

2. Correlated Query : Subquery references columns from the main query.

3. Commont Table Expresions :
	- Like giving a nickname to a query so we can easily use it as a subquery.
	- WITH CTE1 AS (...)

---

#  Query Optimization :

1. Exploding Join : Missing ON condition
2. UNION ALL : If no duplicates.
3. Filters & Limits for faster results.
4. Filter before JOIN Operations.

---
#  Semi-Structured Data :

- Snowflake supports JSON.
- VARIANT DataType to handle JSON Data.
- Pass JSON Data to PARSE_JSON, which returns a JSON object as 'VARIANT' DataType.
- OBJECT_CONSTRUCT (..) : Creates JSON 	Objects from Key-Value Pairs.








