#d 	Signed integer decimal. 	
#i 	Signed integer decimal. 	
#o 	Unsigned octal. 	(1)
#u 	Unsigned decimal. 	
#x 	Unsigned hexadecimal (lowercase). 	(2)
#X 	Unsigned hexadecimal (uppercase). 	(2)
#e 	Floating point exponential format (lowercase). 	
#E 	Floating point exponential format (uppercase). 	
#f 	Floating point decimal format. 	
#F 	Floating point decimal format. 	
#g 	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise. 	
#G 	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise. 	
#c 	Single character (accepts integer or single character string). 	
#r 	String (converts any python object using repr()). 	(3)
#s 	String (converts any python object using str()). 	(4)
#% 	No argument is converted, results in a "%" character in the result.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue' 
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not to heavy."
print "He's hot %r eyes and  %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to het it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + weight + height
)