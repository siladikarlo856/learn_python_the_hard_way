# import module
from sys import argv
# unpack argv parameters
script, filename = argv
# open filename and use variable for object
txt = open(filename)
# print filename which was forwareded using params - argv
print "Here's your file %r:" % filename
# print contetn od txt file
print txt.read()

# print instructions 
print "Type the filename again: "
# get input from user and save it to variable
file_again = raw_input("> ")
# open file "file_again" and use variable to hold object
txt_again = open(file_again)
# print content of txt_again file
print txt_again.read()