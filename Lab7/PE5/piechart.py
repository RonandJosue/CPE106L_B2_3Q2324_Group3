"""
File: piechart.py

Displays a pie chart of monthly living expenses.
"""

import matplotlib.pyplot as plt

# Prepare the data
expenses = {"Rent":1200, "Food":700, "Healthcare":500,
            "Transportation":300, "Utilities":600,
            "Entertainment":200}
labels = list(expenses.keys())
slices = list(expenses.values())

# Set up and show the pie chart
plt.pie(slices, labels = labels, autopct = "%1.1f%%")
plt.title("Pie Chart of Living Expenses")
plt.show()

# Optional pie parameters: rotatelabels <Boolean - False by default>
#                          colors <a list of color values>
#                          startangle <0 (due east) by default, increasing
#                                     counterclockwise>
#                          shadow <Boolean - False by default>
#                          explode <a list of distances from center point>
# Can add a legend by calling plt.legend()

## Color abbreviations
##'r' - Red
##'g' - Green
##'b' - Blue
##'c' - Cyan
##'m' - Magenta
##'y' - Yellow
##'k' - Black
##'w' - White

# Also hex colors in format "#rrggbb"
