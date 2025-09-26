- Python Shell: iPython - Part of Jupyter Ecosystem

- List Slicing: Selecting Multiple Elements from a list. [Inclusive:Exclusive]
- Changing List Elements : fam[0:2] = ["Apple", 1.64]
- y=x : You're copying the reference to the list.
- y=list(x),  y=x[:] : New List Altogather.

- Function : It's a standalone piece of code.
- Methods : Defined inside a class. Used by objects of a class.
- Attributes: Do not have () after them.

- NumPy : Numeric Python - Provides NumPy Array, an alernative to python List. Performs VECTOR Operations (2darray * 2).
	- Creating a np with different types of elements will result in everything converted to strings.
	- bmi[bmi>25]

- 2D Numpy Arrays:
	-2darr[1, 0] or [1][0]
	-2darr[:, 1:3] ~ Both Rows - 4 elements = from Column's 1 & 2
	
- NumPy for Statistics:
	- Mean
		- np.mean(np_city[:, 0])
	- Median
		- np.median(np_city[:, 0])

	- corrcoef, std, sum, sort
	
	- GENERATE DATA ~ np.random.normal(loc=mean, scale=std, size=shape)
	
- Since Numpy enforces a single data type in the array, it has more speed.
