"""
File: scatterplot.py

Displays unique random numbers between 1 and 100, in the
order in which they are generated, in a scatter plot.
"""

import matplotlib.pyplot as plt
import stats

# Prepare the data
positions = list(range(1, 101))
numbers = stats.getRandomList(100, 1, 100, unique = True)

# Set up and show the scatter plot
plt.scatter(positions, numbers,
            color = "purple", marker = '.')
plt.title("Scatter Plot of Unique Random Numbers from 1..100")
plt.xlabel("Position")
plt.ylabel("Random number")
plt.show()

