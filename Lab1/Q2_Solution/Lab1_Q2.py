filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    exit()

num_lines = len(lines)
print("Number of lines in the file:", num_lines)

while True:
    try:
        line_number = int(input("Enter a line number (1 to {}), or 0 to quit): ".format(num_lines)))
        if line_number == 0:
            print("Exiting program.")
            break
        elif 1 <= line_number <= num_lines:
            print("Line {}:".format(line_number), lines[line_number - 1])
        else:
            print("Invalid input. Please enter a number between 0 and {}.".format(num_lines))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# does not work on vsc but online gdb is good
