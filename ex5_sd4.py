inch_to_cm_const = 2.54
lbs_to_kg_const = 0.454

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_height_cm = my_height * inch_to_cm_const
my_weight = 180 # lbs
my_weight_kg = my_weight * lbs_to_kg_const
my_eyes = 'Blue' 
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s" % my_name
print "He's %.2f cm tall." % my_height_cm
print "He's %.2f kg heavy." % my_weight_kg
print "Actually that's not to heavy."
print "He's hot %s eyes and  %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to het it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_weight + my_height
)