x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke = "isn't that joke so funny?! %r"

print joke % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# you can still add strings together despite it being a non-numeric value