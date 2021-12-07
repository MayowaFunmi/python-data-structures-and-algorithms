# compare python list size and numpy size

import time
import sys
# import numpy as np

b = range(1000)
print(sys.getsizeof(5) * len(b))

"""
c = np.arange(1000)
print(c.size * c.itemsize)
"""

# compare python list speed and numpy speed
size = 100000
l1 = range(size)
l2 = range(size)

# for python list
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
result = [(x + y) for x, y in zip(l1, l2)]
#print(result)
print("Python list took:", (time.time() - start) * 1000)


# for numpy
"""
a1 np.arange(size)
a2 = np.arange(size)
start = time.time()
result = a1 + a2
print("Numpy array took:", (time.time() - start) * 1000)
"""
