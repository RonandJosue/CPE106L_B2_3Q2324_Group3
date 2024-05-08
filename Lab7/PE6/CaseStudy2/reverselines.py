"""
File: reverselines.py

Reverses the lines in a CSV file while
keeping the first header line in place.
"""

inFileName = input("Input file name: ")
outFileName = input("Output file name: ")
inFile = open(inFileName, 'r')
lyst = []
header = inFile.readline()
while True:
    line = inFile.readline()
    if line == "":
        break
    lyst.append(line)
lyst.reverse()
outFile = open(outFileName, 'w')
outFile.write(header)
for line in lyst:
    outFile.write(line)
outFile.close()
