tabby_cat = "\tI'm tabbed in." # \t is tab
persian_cat = "I'm split\non a line." # \n is next line
backslash_cat = "I'm \\ a \\ cat." # double backslash makes a \
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
slash_cat = '''
#grumpy'''

formatcat = '''%s''' % backslash_cat

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print slash_cat

print formatcat