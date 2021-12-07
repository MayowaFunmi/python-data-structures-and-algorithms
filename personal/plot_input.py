import matplotlib.pyplot as plt 
import math 
import numpy as np

x = list(map(int(input("Enter values of x separated by single spaces: ").split())))

y = list(map(int(input("Enter values of y separated by single spaces: ").split())))

x_vals = x
y_vals = y

plt.ion()
plt.plot(x_vals, y_vals)
plt.show()