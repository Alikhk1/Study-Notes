# Pandas : 

- Python Package for data manipulation. Can also be used for data visualization.
- It's Built on top of numpy and matplotlib.
- Basic Methods:

		1. .head() ~ Returns first few rows.
		2. .info() ~ Names of Columns, Their Datatypes and any missing values.
		3. .shape ~ Displays (rows, columns).
		4. .describe() ~ calculates a few summary statistics for each column.

- 3 Components of DataFrames:

		1. .values ~ all values.
		2. .columns ~ column names.
		3. .index ~ row names.

---

# Manipulating DataFrames :

1. Sorting :
	
		- .sort_values('column_name', ascending=False) ~ Sorts values ascending order by default.
		- .sort_values(['col1','col2'], ascending=[True, False]) ~ Sorts first by col1 and then by col2.
		 

2. Subsetting :

	1. Columns :

			- dogs['name'] ~ Displays values in the column.
			- dogs[['name', 'heigth']] ~ Outter Brackets Subset, while inner is a List of columns to subset.

	2. Rows :

			- Most common way is to create a logical condition to filter against.
			- dogs[dogs['heigth'] > 50] 
			- dogs[dogs['name'] == 'Labrador']
			- dogs[dogs['DOB'] < '2025-01-01'] ~ YYYY-MM-DD International Standard.
			- lab = dogs['name'] == 'Labrador' , shep = dogs['name'] == 'shephard' , dogs[lab & shep]
			- .isin() ~ dogs[dogs['color'].isin(['Black','Brown'])] ~ List of values to filter for.
		

3. Adding New Columns:

		- dogs['heigth_in_meters'] = dogs['heigth'] / 100 ~ creates a new column.


---

# Summary Statistics :
	
1. NUMERIC :

		- dogs['name'].mean() , median, mode, min, max, var, std, sum, quantile, cumsum, cummax, cummin, cumprod.	
		- .mean(axis='index'/'columns')
		- .agg() ~ generate custom statistics on multiple columns with multiple functions - dogs[['name', 'height']].agg([function1, 'median']) 
		
2. STRING : COUNTING

		- DROP DUPLICATES: dogs.drop_duplicates(subset=['name', 'breed'])
		- COUNTING : dogs['name'].value_counts(sort=True, normalize=True) ~ Normalize turns counts into proportions of total.
		
3. Group Summaries :
		
		- dogs[dogs['color'] == 'black]['weight'].mean()
		- GROUPBY: dogs.groupby('color')['weight'].mean() ~ Does the same thing as above but for all colors.
		- Multiple Columns: dogs.groupby(['color','breed'])[['weights, 'height']].mean()

4. Pivot Tables :
	
		- Pivot Tables are just DataFrames with sorted Indexes.
		- dogs.pivot_table(values='weight_kg', index='color', columns='breed', aggfunc=['median','mean'], fill_value=0, margins=True)
		- Values is columnn you want to summarize, index is column you want to groupby, by default it takes mean. Columns is values of columns.
		- Shows empty values aswell, filled by fill_value.

---

# Splitting & Slicing DataFrames :

1. INDEXES :

		1. SET COLUMN AS INDEX: dogs = dogs.set_index('name')
		2. RESET INDEX: dogs.reset_index(drop=True), the index column would be dropped & replaced with (0,1,2..,n)
		3. Index values don't have to be unique.
		4. By Setting Index, .loc can work directly on column name. SORTING INDEX: .sort_index()		
		5. SYNTAX FOR WORKING WITH INDEXES IS DIFFERENT THAN COLUMNS.


2. LOC & ILOC :
		
		- For indexed OUTTER COLUMN : dogs.loc['row1':'row2']
		- For indexed INNER COLUMN  : dogs.loc[('col1','col2'):('col1':'col2)]


3.  CALCULATIONS ON PIVOT TABLES :

		- INDEX STUFF WORKS ON PIVOT TABLES.
		- .loc["row1":"row2"] IS IDEAL FOR SUBSETTING PIVOT TABLE.


---

# Visualizing DataFrames : (WITH MATPLOTLIB)

	- HISTROGRAM : dogs['height'].hist()
	- BAR CHART (relation b/w numeric & category data) : average_weight.plot(kind="bar", title="")
	- LINE PLOT (changes over time) : dog.plot(x='date', y='weight', kind="line")
	- SCATTER PLOT (relation b/w 2 numeric varaibles) : dog.plot(x="height", y="weight", kind="scatter")
	- LAYERING PLOTS : 
		- dogs[dogs['breed']='labrador']['height'].hist()
		- dogs[dogs['breed']='Shepherd']['height'].hist()
		- plt.legends(['L','S'])	
---

# MISSING VALUES :
	1. CHECK IF MISSING VALUES :
		- .ISNA() : True If value is NaN
		- .ISNA().ANY() : Shows columns with NaN
		- .ISNA().SUM() : Number of missing values

	2. REMOVE MISSING ROWS :
		- .DROPNA()

	3. FILL MISSING VALUES :
		- .FILLNA(0)
---

# CREATING DATAFRAMES :

	1. List of Dictionaries : Data built row by row
		- [{name,weight},{name,weight}]
		- pd.DataFrame(list_of_dicts)

	2. Dictionary of Lists : Data built column by column
		- {key:list,key:list}
		- pd.DataFrame(dict_of_lists)
	

---

# READING & WRITING CSV :

	1. read_csv()
	2. to_csv()































































