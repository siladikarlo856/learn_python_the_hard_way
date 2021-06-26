from sys import argv

# store command line arguments into variables
script, input_file = argv

# function to print whole file 
def print_all(f):
    print f.read()

# function to rewind file
def rewind(f):
    f.seek(0)

# function to print line
def print_a_line(line_count, f):
    print line_count, f.readline()

# open file which name was provided as cmd line parameter
current_file = open(input_file)

print "First let's print the whole file:\n"
# print whole file using function print_all()
print_all(current_file)

print "Now, let's rewind, kind of like a tape."
# rewind file using function rewind(file) 
rewind(current_file)

print "Lets print three lines:"
# set variable current line value to 1
current_line = 1
# print a line using function print_a_line(line_cnt, file)
print_a_line(current_line, current_file)

# set variable current line value to 1 + 1 = 2
current_line += 1
# print a line using function print_a_line(line_cnt, file)
print_a_line(current_line, current_file)

# set variable current line value to 2 + 1 = 3
current_line = current_line + 1
# print a line using function print_a_line(line_cnt, file)
print_a_line(current_line, current_file)
