"""
File: pandasplots.py

Illustrates plotting operations in pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

# Create a data frame and a simple line plot
data = {"Course":["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment":[40, 32, 19]}
frame = pd.DataFrame(data)
print(frame)
frame.plot(marker = 'o')
plt.show()

# Create a data frame with labeled indexes and a line plot
# and horizontal bar plot
data = {"Course":["CSCI112", "CSCI312", "PHIL258"],
        "Enrollment":[40, 32, 19]}
frame = pd.DataFrame(data, index = data["Course"])
print(frame)
frame.plot(marker = 'o')
plt.show()
frame.plot.barh()
plt.show()


