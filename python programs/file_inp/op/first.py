# Opening and reading a file in Python
# Using open() function to open a file and read its content

f = open("demo1.txt", "r")  # Open file in read mode
data = f.read()  # Read the content of the file
print(data)  # Print the content of the file

# reads one line at a time

line1 = open("demo1.txt", "r").readline()  # Read the first line of the file
print(line1)  # Print the first line
# Read the first line of the file again
line2 = open("demo1.txt", "r").readline()
print(line2)  # Print the first line again
# Read all lines of the file and store them in a list
line3 = open("demo1.txt", "r").readlines()
print(line3)  # Print the list of lines
f.close()  # Close the file