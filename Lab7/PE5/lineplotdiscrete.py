"""
File: lineplotdiscrete.py

Displays values of y = x * 2 and y = x ** 2,
for a discrete range of x = 1..5, in line plots.
"""

import matplotlib.pyplot as plt
        
# Prepare the data
xValues = list(range(1, 6))
doubles = list(map(lambda x: x * 2, xValues))
squares = list(map(lambda x: x ** 2, xValues))

# Set up and show the line plots
plt.plot(xValues, doubles, label = "y = x * 2",
         color = "blue", marker = 'o')
plt.plot(xValues, squares, label = "y = x ** 2",
         color = "red", marker = 'o')
plt.xticks(xValues)
plt.title("Line Plots of Doubles and Squares of Discrete Values 1..5")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()
