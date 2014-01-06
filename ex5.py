# -- coding: utf-8 --

my_name = "Alex Kopel"
my_age = 26 # not lying
my_height = 70 # inches
my_weight = 170 # pounds
my_eyes = 'Brown'
my_teeth = 'White'
my_hair= 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the cofee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
	
birth = [11,12,1987]

print "My birthday is %r." % birth

print "My birthday is %s." % birth