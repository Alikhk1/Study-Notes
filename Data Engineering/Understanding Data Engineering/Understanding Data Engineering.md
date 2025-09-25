# Data Engineering

**Data Engineering** is the process of transforming data into a format suited for analysis.

## Data Workflow
1. **Collection & Storage**
2. **Data Preparation**
3. **Exploration & Visualization**
4. **Experimentation & Prediction**

## Data Engineers
Data Engineers are responsible for the 1st step. They lay the groundwork for Data Scientists, Analysts & ML Engineers.

- **Role**: Deliver the correct Data, in the right Form, to right people as efficiently as possible.
- **Skills**: Software experts (while Data scientists are analysts).
- **Tasks**:
    - Ingest Data from different sources.
    - Optimize databases for analysis.
    - Remove corrupted data.
    - Develop, construct, test and maintain Data architectures such as databases and large scale processing systems.

## Big Data
### The Five V's:
1. **Volume** (how much)
2. **Variety** (what kind)
3. **Velocity** (how frequent)
4. **Veracity** (how accurate)
5. **Value** (how useful)

## Data Pipeline
- **Process**: Ingest, Process, Store.
- **Purpose**: Automate flow from one station to the next.
- **ETL**: Popular framework for designing data pipelines.

## Data Structure

### 1. Structured
- Strict schema
- Relational databases, CSV files.

### 2. Semi-Structured
- No fixed schema but organized (tags or keys)
- Examples: XML, JSON, YAML.

### 3. Unstructured
- Examples: Images, Videos, Sounds.

## Data Lakes vs Warehouses

### Data Lake
- **Content**: Unprocessed/Messy
- **Size**: PetaBytes
- **Data Types**: All data types
- **Cost**: Cost Effective
- **Data Catalog**: Source? Use? Owner? How often updated? (Ensures reproducibility)
    - **No Catalog** = **Data Swamp**
- **Users**: Data Scientists for Big Data & Real Time analytics.

### Data Warehouse
- **Content**: Specific data for specific use
- **Size**: Relatively small
- **Data Types**: Structured Data
- **Updates**: Costly to update
- **Users**: Data Analysts.

## Scheduling

- **Batches**: Grouping records and updating at intervals. Cheaper.
- **Stream**: Individual records sent right away.
- **Tools**: Apache AirFlow.

## Parallel Computing

- Basis of modern data processing tools.
- **Approach**: Several smaller subtasks → Run on several computers.