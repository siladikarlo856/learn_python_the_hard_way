from sys import argv

# Let's see how "unpacking" wroks
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

y = raw_input("Write something: ")
print "You wrote:", y
