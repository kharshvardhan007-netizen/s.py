#standard python list(slow)
#python_list = list(range(1000000))
#result = [x + 2 for x in python_list]#apply loop evey item


#numpy array (50x-100x faster)
import numpy as np 

np_array = np.arange(1000000)
result = np_array +2 #continuos c- code execution