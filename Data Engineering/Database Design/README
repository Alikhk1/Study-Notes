# Database Design and Data Processing Notes

## Database Design
- Depends on how data will be used.

---

## Approaches to Data Processing
Defines how data is going to flow, be structured, and stored.

### OLTP (Online Transaction Processing)
- Supports daily transactions.  
- Operational databases.  
- Highly normalized, write-intensive.  
- Example: Find price of a book.  

### OLAP (Online Analytical Processing)
- Supports business decision-making, reporting, and data analysis.  
- Data warehouses.  
- Less normalized, read-intensive.  
- Example: Calculate books with best profit margin.  

---

## Data Structures
1. **Structured Data**: Schema-defined with datatypes and relationships (e.g., SQL, tables).  
2. **Unstructured Data**: Schema-less (e.g., photos, videos, MP3).  
3. **Semi-Structured Data**: Self-describing structure, no rigid schema (e.g., NoSQL, XML, JSON).  

---

## Data Storage Architectures
- **Data Lakes**: Store all data types (structured, unstructured, semi-structured). Object storage for Big Data analysis.  
- **Data Swamp**: Uncatalogued, unmanaged data lake.  
- **Data Warehouses**: Optimized for OLAP.  
- **Data Marts**: Subset of warehouses, focused on specific topics.  

---

## Data Integration Workflows

### ETL (Extract, Transform, Load)
- Transform data (clean, aggregate, standardize) on an ETL server.  
- Load transformed data into a warehouse.  
- Common in legacy systems, strict schema control, or complex transformations.  

### ELT (Extract, Load, Transform)
- Extract data from sources.  
- Load raw data into a warehouse or data lake.  
- Transform data using system compute (SQL, Spark, etc.).  
- Common in modern cloud frameworks.  

---

## Schema
Logical structure that defines how data is organized in a database or warehouse (tables, fields, relationships).

- **Schema-on-read**: Data stored raw; structure applied when accessed.  
- **Schema-on-write**: Data must conform to predefined schema before storage.  

### Schema Types
1. **Star Schema**:  
   - Central Fact table with Dimension tables.  
   - Simple, fast queries.  
2. **Snowflake Schema**:  
   - Normalized dimensions.  
   - Reduces redundancy, increases join complexity.  
3. **Galaxy Schema (Fact Constellation)**:  
   - Multiple Fact tables sharing Dimension tables.  
   - Handles complex analytics across domains.  

---

## Data Modelling
Process of creating data models for storage.  

1. **Conceptual Data Model**: Entities, relationships, attributes. (e.g., ERD, UML)  
2. **Logical Data Model**: Tables, columns, relationships. (e.g., database schemas)  
3. **Physical Data Model**: Physical storage (partitions, backups).  

---

## Dimension Modelling
- Optimized for data warehouses and OLAP.  
- Built on Star Schema.  
- Organizes data into
