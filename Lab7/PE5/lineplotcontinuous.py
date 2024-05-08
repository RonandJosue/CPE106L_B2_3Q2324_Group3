"""
File: lineplotcontinuous.py

Displays values of y = x * 2 and y = x ** 2,
for a continuous range of x = 1..5, in line plots.
"""

import matplotlib.pyplot as plt
import numpy as np
        
# Prepare the data
xValues = np.linspace(1, 5)
doubles = xValues * 2
squares = xValues ** 2

# Set up and show the line plots
plt.plot(xValues, doubles, label = "y = x * 2",
         color = "blue")
plt.plot(xValues, squares, label = "y = x ** 2",
         color = "red")
plt.title("Line Plots of Doubles and Squares of Continuous Range 1..5")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()
