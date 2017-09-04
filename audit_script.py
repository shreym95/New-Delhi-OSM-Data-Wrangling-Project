import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
import re

# Dictionary to count various tags
def count_tags(filename):
    tag_dict = {}
    for event,elem in ET.iterparse(filename):
        if elem.tag in tag_dict:
            tag_dict[elem.tag] += 1
        else:
            tag_dict[elem.tag] = 1
    return tag_dict

# Finding various attributes for xml tags
def find_attributes(filename):
    attribute_dict = defaultdict(set)
    for event, element in ET.iterparse(filename):
        for each_attrib in element.attrib :
            attribute_dict[element.tag].add(each_attrib)

    return attribute_dict

# Making a dictionary to overview "<tag>" attributes data and values
def  find_tag_keys_vals(filename):
     tag_key = defaultdict(set)
     for _,element in ET.iterparse(filename):
         if element.tag=="way":
             for child in element.iter("tag"):
                tag_key[child.attrib["k"]].add(child.attrib["v"])

     return tag_key


# Similar to course material -------------------------------------------------
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

def key_type(element, keys):
    if element.tag == "tag":
        if lower.match(element.attrib["k"]):
            keys["lower"] +=1
        elif lower_colon.match(element.attrib["k"]):
            keys["lower_colon"] +=1
        elif problemchars.match(element.attrib["k"]):
            keys["problemchars"] +=1
        else:
            print(element.attrib["k"])
            keys["other"] +=1

    return keys
# Ends here ---------------------------------------------------------------------------

# Finding tags with multiple fields such as "addr:housenumber"
def secondary_tags(filename):
    compile_seconds = defaultdict(set)
    for _, element in ET.iterparse(filename):
        if element.tag == "tag":
            for key in element.attrib:
                value = element.get(key)
                key_pairs = value.split(":")
                if len(key_pairs) == 2:
                    compile_seconds[key_pairs[0]].add(key_pairs[1])
    return  compile_seconds

# Overview of fields containing street names
def street_names(filename):
    streets = []
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":
            for each in element.iter("tag"):
                if each.get("k") in ["addr:street","addr:full", "name"]:
                    streets.append(each.attrib["v"])
    return streets

# Overview of fields containing phone numbers
def phone_numbers(filename):
    numbers = []
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":
            for each in element.iter("tag"):
                if each.get("k") in ["contact:phone", "contact:mobile", "phone"]:
                    ## add check for mobile or not and create dictionary
                    numbers.append(each.attrib["v"])
    return numbers

# Auditing source names and their counts
def source_names(filename):
    sources = {}
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":
            for each in element.iter("tag"):
                if each.get("k") == "source":
                    if each.get("v") in sources:
                        sources[each.get("v")] += 1
                    else:
                        sources[each.get("v")] = 1
    return sources

# Checking out postal codes
def post_codes(filename):
    codes = set()
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":
            for each in element.iter("tag"):
                if each.get("k") == "addr:postcode":
                    codes.add(each.get("v"))
    return codes

pprint.pprint(count_tags("delhi_map.osm"))