"""
File: barcharthorizontal.py

Displays enrollments in three courses
in a horizontal bar chart.
"""

import matplotlib.pyplot as plt
import numpy as np
 
# Prepare the data
data = {"Data\nStructures":40,
        "Programming\nLanguage\nDesign":32,
        "Freud\nSeminar":19}
courses = list(data.keys())
enrollments = list(data.values())

# Set up and show the bar chart
plt.figure(figsize = (10, 4))
plt.barh(courses, enrollments, height = 0.2)
plt.title("Students Enrolled in Ken's Courses")
plt.xlabel("Number of students")
plt.ylabel("Course")
plt.show() 



