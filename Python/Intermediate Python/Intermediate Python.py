#--------------------------------------------------- MATPLOTLIB --------------------------------------------------
import matplotlib.pyplot as plt
years = [2002, 2010, 2020, 2025]
pop = [2.1, 3.4, 4.5, 8.2]

#=======> Line Graph   <=======
plt.plot(year , pop) # First argument is horizontal x-axis
plt.show()
# Axis Labels:
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population')
# Axis Scale:
plt.yticks([0,2,4,8,10],
           ['0','2B','4B','8B','10B']) # (Scale, Display names of ticks)

#=======> Scatter Plot <=======
plt.scatter(gdp , life_exp, size = pop, c=color, alpha = 0.8) # alpha is opacity.
 # Individual dot labels:
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
# Changing x-axis to log scale:
plt.xscale('log')
# Adding a grid:
plt.grid(True)
plt.show()

#=======>  Histrogram  <=======
values=[1,2,3,4,5,6,7,8,9,10]
plt.hist(values,bins=3)

#--------------------------------------------------- PANDAS --------------------------------------------------
import pandas as pd
#=======>  DataFrame From Dict  <=======
dataframe = pd.DataFrame(dict) # Key : List
# Add Labels:
dataframe.index = ['BR','IN','EN','RU','CH','SA']

#=======>  CSV to DataFrame  <=======
brics = pd.read_csv('path/csv', index_col = 0) # Which Column to use as index, by default DataFrame inserts indexes at col 0.

#=======>  Accessing Data  <=======
brics[['country', 'capital']]
# Rows:
brics[1:4]  
# loc:
brics.loc[["RU", "IN", "CH"]] 
brics.loc[["RU", "IN", "CH"], ["country", 'capital']] # countries and list of column labels we want, (row labels, column labels)
brics.loc[:,["country", 'capital']] # all rows
# iloc: # just like loc but with indexes.
brics.iloc[[1]]

#=======>  Filtering Data  <=======
# Suppose we want countries with areas greater than 8
is_huge = brics['areas'] > 8 # perform this on a series not dataframe, returns a boolean series.
brics[is_huge] # we will get series with countries areas > 8 

# Suppose we only want to keep countries within a specific area range
import numpy as np
np.logical_and(brics['area'] > 8, brics['area'] < 10) # 8 < areas < 10
brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]  # Putting this code to Subset appropiately

#=======>  Iterating Over DataFrame  <=======

# In pandas you have to mention explicitly that you want to iterate over the rows:
import pandas as pd
for lab, row in brics.iterrows(): # iterrows() methods generates a label and row data
    print(lab)
    print(row)
# Creating a new column with the lenght of the country's name:
for lab,rows in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])

# Better way to do the above is to use "apply" function :
brics['name_length'] = brics['country'].apply(len) 

#--------------------------------------------------- Random Numbers --------------------------------------------------
import numpy as np
np.random.seed(123) # Same seed: same random numbers
np.random.rand()
np.random.randint(0,2) # Generates 0 or 1
