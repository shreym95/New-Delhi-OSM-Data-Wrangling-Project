import re

# To check valid Street Name fields
def is_street_field(field):
    if field in ["addr:street", "addr:full", "name", "street"]:
        return True
    else:
        return False

# Regex Patterns to match certain street name abbreviations
ext_match = re.compile(r'([Ee]xt(,|n)$)')
st_match = re.compile(r'St$')
mkt_match = re.compile(r'[Mm]kt$')
rd_match = re.compile(r'Rd$')
sec_match = re.compile(r'Sec$')
ave_match = re.compile(r'Ave$')

##Function to capitalize first letter of each word, bypassing pitfalls of .title()
##Taken from this thread: "https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python"
def repl_func(m):
    return m.group(1) + m.group(2).upper()


def correct_streets(name):
        # Capitalize first letter of each word
        name_new = re.sub("(^|\s)(\S)", repl_func, name)

        # Various regex patterns for abbreviations, as location of such words is not predictable in Street Name in most of the cases
        if ext_match.search(name_new) is not None:
            name_new = ext_match.sub("Extension", name_new)
            #print(name + " => " + name_new)
        elif st_match.search(name_new) is not None:
            name_new = st_match.sub("Street", name_new)
            #print(name + " => " + name_new)
        elif mkt_match.search(name_new) is not None:
            name_new = mkt_match.sub("Market", name_new)
            #print(name + " => " + name_new)
        elif rd_match.search(name_new) is not None:
            name_new = rd_match.sub("Road", name_new)
            #print(name + " => " + name_new)
        elif sec_match.search(name_new) is not None:
            name_new = sec_match.sub("Sector", name_new)
            #print(name + " => " + name_new)
        elif ave_match.search(name_new) is not None:
            name_new = ave_match.sub("Avenue", name_new)
            #print(name + " => " + name_new)
        return name_new