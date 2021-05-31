# How to add integer value into string
x = "There are %d types of people." % 10
# String stored in variable
binary = "binary"
# single quote inside string
do_not = "don't"
# Add two variables into string
y = "Those who know %s and those who %s." % (binary, do_not)

# printing variables
print x
print y

# print string which cobines two strings one through repr()
print "I said: %r." % x
# Insert variable value inside quotes in another string.
print "I also said: '%s'." % y

# boolean value
hilarious = False
# variable with placeholder for value
joke_evaluation = "Isnt that joke so funny?! %r"

# printing string where formatting is done in variable value
print joke_evaluation % hilarious

# two strings
w = "This is the left side of..."
e = "a string with a right side."

# combining strings using + sign
print w + e
