"""
File: histogram.py

Displays frequencies of 50 random scores between 95 and 100
in a histogram.
"""

import matplotlib.pyplot as plt
import stats
        
# Prepare the data
scores = stats.getRandomList(50, 95, 100)

# Set up and show the histogram
plt.hist(scores, width = .2)
plt.title("Frequencies of 50 random scores between 95 and 100.")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()
