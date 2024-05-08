"""
File: stats.py

Defines functions to compute the mean, median, std, and mode
of a list of numbers.
"""

import math
import random

def mean(lyst):
    """Returns the mean of a list of numbers."""
    return sum(lyst) / len(lyst)

def frequencies(lyst):
    """Returns a dictionary keyed by the unique
    numbers and their frequencies in lyst."""
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for number in lyst:
        freq = theDictionary.get(number, 0)
        theDictionary[number] = freq + 1
    return theDictionary

def mode(lyst):
    """Returns the mode of a list of numbers."""
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result = key
            break
    return result

def modes(lyst):
    """Returns the modes of a list of numbers."""
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    result = []
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result.append(key)
    return result

def median(lyst):
    """Precondition: lyst is non-empty.
    Returns the median of numbers in lyst."""
    if len(lyst) == 0: 
        raise RuntimeError("List must be non-empty. ")
    copy = list(lyst)
    copy.sort()
    midpoint = len(lyst) // 2
    if len(lyst) % 2 == 1:
        return copy[midpoint]
    else:
        return mean([copy[midpoint - 1], copy[midpoint]])

def std(lyst):
    """Precondition: lyst is non-empty.
    Returns the standard deviation of the numbers in lyst."""
    if len(lyst) == 0: 
        raise RuntimeError("List must be non-empty. ")
    average = mean(lyst)
    differences = map(lambda x: x - average, lyst)
    squares = list(map(lambda x: x ** 2, differences))
    return math.sqrt(mean(squares))

def getRandomList(size, lower, upper, unique = False):
    """Returns a list of randomly generate numbers
    within the given bounds."""
    theList = []
    for count in range(size):
        number = random.randint(lower, upper)
        if unique:
            while number in theList:
                number = random.randint(lower, upper)
        theList.append(number)
    return theList

def main():
    """Tests the functions."""
    lyst = [3, 1, 7, 1, 4, 10]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))
    print("Standard deviation:", std(lyst))    
    print("Frequencies:", frequencies(lyst))
    lyst.sort()
    print(lyst)
    lyst = [3, 1, 7, 1, 4]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))
    print("Standard deviation:", std(lyst))    
    print("Frequencies:", frequencies(lyst))
    lyst.sort()
    print(lyst)
    lyst = getRandomList(10, 1, 10)
    print(lyst)
    lyst = getRandomList(10, 1, 10, unique = True)
    print(lyst)
    

# The entry point for program execution
if __name__ == "__main__":
    main()
     
    
        
