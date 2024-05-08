"""
File: barchartvertical.py

Displays enrollments in three courses
in a vertical bar chart.
"""

import matplotlib.pyplot as plt
 
# Prepare the data
data = {"CSCI112":40, "CSCI312":32, "PHIL258":19}
courses = list(data.keys())
enrollments = list(data.values())

# Set up and show the horizontal bar chart
plt.figure(figsize = (4, 4))
plt.bar(courses, enrollments, width = 0.2)
plt.title("Students Enrolled in Ken's Courses")
plt.xlabel("Course")
plt.ylabel("Number of students")
plt.show()



