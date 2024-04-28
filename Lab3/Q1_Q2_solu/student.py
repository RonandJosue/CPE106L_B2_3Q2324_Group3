"""
File: student.py
Resources to manage a student's name and test scores.
This file contains the answer for both 1 and 2
"""
import random
class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    
    def __eq__(self, other):
        """Tests for equality based on student names."""
        return self.name == other.name
    
    def __lt__(self, other):
        """Tests if self's name is less than other's name."""
        return self.name < other.name
    
    def __ge__(self, other):
        """Tests if self's name is greater than or equal to other's name."""
        return self.name >= other.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    students = [
        Student("Ken", 5),
        Student("Alice", 5),
        Student("Bob", 5),
        Student("Charlie", 5),
        Student("David", 5)
    ]
    random.shuffle(students)
    
    students.sort(key=lambda x: x.name)
    
    for student in students:
        print(student)
        print()

    print("Testing equality:")
    print("student1 == student2:", students[1] == students[1])
    print()
    
    print("Testing less than:")
    print("student1 < student2:", students[1] < students[2])
    print("student2 < student1:", students[2] < students[1])
    print()
    
    print("Testing greater than or equal to:")
    print("student1 >= student2:", students[1]>= students[2])
    print("student2 >= student1:", students[2] >= students[1])

if __name__ == "__main__":
    main()

