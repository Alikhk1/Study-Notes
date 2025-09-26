# Matplotlib
	- import matplotlib.pyplot as plt
	- Line, Scatter graphs, Histrograms.

# Pandas : High-Level Data Manipulation tool, Built on NumPy

	- NumPy arrays only have one data type.
	- Pandas is Tabular Data.	

	- Steps:
		1. Create a Dict (Key,List) pairs.
		2. import pandas as pd
		3. dataframe = pd.DataFrame(dict) OR brics = pd.read_csv('path/csv', index_col = 0)

	- loc: Select parts of data based on labels.
	- iloc: Select data based on position.

	- FILTERING:
		1. Select column -> brics["areas"] 
		2. Do comparison -> is_huge = brics['areas'] > 8
		3. Use this to select -> brics[is_huge]
 

# Numpy : 
	- Logical Operations on arrays:
		- np.logical_and(bmi > 21, bmi < 22) ~ gives an array of true/false.
		- bmi[np.logical_and(bmi > 21, bmi < 22)] ~ gives an array of values which are true.

	- Iterate over:
		- for val in np.nditer(nparray) ~ prints out elements row by row.

# Random Numbers :
	- import numpy as np 
	- np.random.rand()
