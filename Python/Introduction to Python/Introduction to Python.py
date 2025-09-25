import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height ** 2

# Using Booleans to Subset numpy
bmi > 25 # Prints all elements with True/False 
bmi[bmi > 25] # Now only elements with bmi > 25 are printed