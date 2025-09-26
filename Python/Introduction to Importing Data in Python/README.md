
#  Flat Files : Simple files that store data in plain text without Hierarchical Structures. - .txt .csv .tsv


- Ways to Open a File :

		1. filename = r"Path"
		   file = open(filename, mode="r") # r = reading mode

		2. with open(r'Path', "r") as file:
		   print(file.read())

	- Best Practice is to use with statement so we don't have to close the file manually.

- Numpy Arrays : Standard for opening numerical data. Numpy is essential for sci-kit learn.

		1. loadtxt() : data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2], dtype=str) # usecols is a list of columns you want to keep.
		2. genfrmtxt() : Can handle missing values, mixed data types, and headers.

	- Numpy Arrays Don't have 2 Dimensional labeled data structure.

- Pandas DataFrames : Slice, Reshape, Groupby, Join, Merge. Perform statistics in a missing value friendly manner. Works with Time-Series Data.
	- Useful in all steps of Data Science :

			1. EDA.
			2. Data wrangling.
			3. Data Preprocessing.
			4. Building models.
			5. Visualizations.

	- Can Import : Relational Database Files, hdf5, MATLAB, Excel Files.
	
	- data = pd.read_csv(file, nrows=5 , header=None, sep="\t", comment="#", na_values=['Takes a List of Strings to treat as Na/NaN'])


---

#  Other Files : Pickled files, Excel Files, SAS and Stata files, HDF5 files, a file type for storing large quantities of numerical data, and MATLAB files.


- Pickled Files : 
	- Serialize : Convert the object to series of bytes (Bytestream).
		- import pickle

	  		 with open(filename, 'rb') as file: 
				data = pickle.load(file)
		
	
- Excel Files :
	-	import pandas as pd
	   data = pd.ExcelFile('Path/filename')
	   print(data.sheet_names)
	   df1 = data.parse(0) # Use indexing to access that particular sheet.	
	   df2 = xls.parse(1, usecols=[1], skiprows=[1], names=['Col1','Col2'])

- SAS/Stata Files : Statistical Analysis Systems (SAS) : Business Analytics Biostatistics
	1. sas7bdat - Database Files :
	> from sas7bdat import SAS7BDAT   
	with SAS7BDAT(filename) as as file: 
		df = file.to_data_frame()
	2. .sas7bcat - Catalog Files
			- 
- Stata : Academic Social Sciences Research.
	1. .dta :
		- df = pd.read_stata('file.dta')

- HDF5 : Hierarchal Data Format 5
	- Standard for storing large quantities of numerical data.
	- HDF5 exabytes
	
	1. import h5py
	   data = h5py.File(filename, 'r') 
	
- MATLABS : Matrix Laboratory. 
	- .mat files are just a collection of objects/variables.
	- So loading a MATLAB file we will get a dict object. The keys are MATLAB variable names and values = objects assigned to those variables.

	1. import scipy.io
	   mat = scipy.io.loadmat(filename)

---
#  Working with Relational Databases in Python

- Python doesn't speak SQL directly.
- You need a database driver/engine like SQLAlchemy.
	1. Open a connection.
	2. Translate Python commands into SQL queries.
	3. Manage sessions & transactions.

1. CONNECTING USING sqlite & Pandas :

	1. CONNECTING (sqlite & pandas):
		- from sqlalchemy import create_engine
	  	  import pandas as pd
	  	  engine = create_engine('sqlite:///[DATABASE_NAME].sqlite')
	  	  con = engine.connect()
	  
	2. Querying Relational Database:
		- rs = con.execute("SELECT * FROM Orders")

	3. Save Results to a DataFrame 
		- df = pd.DataFrame(rs.fetchall())
		- df.columns = rs.keys()
		- print(df.head())

	4. Close the connection.
		- con.close()


	- OR YOU CAN USE WITH CONTEXT MANAGER:
		1. engine = create_enginge('sqlite:///[DATABASE_NAME].sqlite')
		2. with engine.connect() as con:
	 		rs = con.execute('SELECT * FROM Orders")
			df = pd.DataFrame(rs.fetchmany(size=5))
			df.columns = rs.keys()

2. CONNECTING Directly with Pandas :
	- engine = create_engine('sqlite:///[DATABASE_NAME].sqlite')	
	- df = pd.read_sql_query("SELECT * FROM Orders", engine)











