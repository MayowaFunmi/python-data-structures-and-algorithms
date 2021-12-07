import matplotlib.pyplot as plt 
import math 
import numpy as np

x_vals = np.linspace(0,20,20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
plt.plot(y_vals, x_vals)
plt.show()