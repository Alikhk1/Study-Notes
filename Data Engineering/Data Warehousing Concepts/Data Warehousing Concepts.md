# Data Warehousing Notes

## What is Data Warehousing?
- A computer system designed to store and analyze large amounts of data for an organization.  
- Functions:
  - Gathers data from different areas of an organization.  
  - Integrates and stores the data.  
  - Makes the data available for analysis.  

## Why are Data Warehouses Valuable?
1. Support Business Intelligence activities.  
2. Enable effective organizational analysis and decision-making.  

---

## Database Warehouse Layers
1. **Source**  
2. **Staging**: Temporary storage for extracted raw data. Performs data cleaning, validation, and transformation.  
3. **Storage**: Central repository for storing data (Data Warehouse).  
4. **Presentation**: Tools for querying, reporting, dashboards, and OLAP analysis.  

---

## Database Warehouse Methodology
1. **Bill Inmon (Top-down)**  
   - Enterprise Data Warehouse first.  
   - Normalized (3NF) model.  
   - Data marts built later.  

2. **Ralph Kimball (Bottom-up)**  
   - Start with data marts.  
   - Star schema, denormalized.  
   - Combine marts into Data Warehouse.  

---

## Database Warehouse - Data Modelling
- **Fact Table**: Contains measurements, metrics, or facts about an organization. Each column captures a metric about one process/transaction.  
- **Dimension Table**: Describes the attributes in the Fact table. Uses columns from the Fact table as primary keys.  

### Schema Types
- **Star Schema**  
  - Central Fact table with one or more Dimension tables.  
  - Few joins, fast, and easy to use.  

- **Snowflake Schema**  
  - At least one Dimension table does not directly connect with the Fact table.  

### Kimball’s 4-Step Process to Design Star & Snowflake Schemas
1. Select organizational process and ask business questions.  
2. Declare the Grain: Define what a single row in the fact table represents.  
   - Lowest or most detailed level.  
   - Enables aggregation to higher levels when needed.  
3. Identify the Dimensions: Dimensions that apply to each row.  
   - Example:  
     - Time: year, quarter, month  
     - Users: name, email  
   - Answer: “How to describe the data?”  
4. Identify the Numerical Facts for each Fact table row.  
   - Answer: “What are we measuring/answering?”  

### Slowly Changing Dimensions (Kimball’s Approach)
1. **Type 1**: Update old values (overwrite).  
2. **Type 2**: Create a new ID for the updated category, keep the old version as well.  
3. **Type 3**: Add a new column (e.g., Current Model, Previous Model).  

---

## Data Integration

### ETL (Extract, Transform, Load)
- **Advantages**  
  1. Lower data storage cost.  
  2. Easier compliance with Personal Identifiable Information (PII).  

- **Disadvantages**  
  1. Transformation errors or changes require new data pulls.  
  2. Requires a separate system to process data.  

### ELT (Extract, Load, Transform)
- **Advantages**  
  1. No separate system needed to process data.  
  2. Transformations can be rerun without impacting source systems.  
  3. Supports near real-time requirements.  

- **Disadvantages**  
  1. Increased storage needs from raw data.  
  2. PII compliance can be more complex.  

---

## Data Cleaning
1. **Data Format Cleaning**: Standardize dates, capitalization, naming.  
2. **Address Parsing**: Split street addresses into components.  
3. **Data Validation**: Apply range checks, type checks, and consistency checks.  
