## IMPORTS! #############################
import xml.etree.cElementTree as ET
import codecs
import json
import re

# Field wise cleaning functions split into different files
from street_clean import correct_streets, is_street_field
from number_clean import correct_number_format, is_phone_field
from extra_cleaning_funcs import modify_state, modify_source
##########################################


CREATED = ["version", "changeset", "timestamp", "user", "uid"]
INIT_INFO = ["id", "visible"]

problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# --**##### Cleaning algorithms begins here #####**--
def contains_attrib(att, element):
    if att in element.attrib:
        return True
    else:
        return False

def cleaning_tech(key, val):            # All specific fields related cleaning of data
    # CHECK 1
    if is_street_field(key):
        correct_value = correct_streets(val)
    elif key == "addr:state":
        state = val
        correct_value = modify_state(state)
    # CHECK 2
    elif is_phone_field(key):
        correct_value = correct_number_format(val)
    # CHECK 3
    elif key == "addr:postcode":
        code = val
        temp = re.sub(r'-|:|\s|/', "", code)
        if len(code) == 6:
            correct_value = temp
        else:
            correct_value = "NaN"       # Incorrect postcode size not allowed in final data
    # CHECK 4
    elif key == "source":
        source = val
        correct_value = modify_source(source)
    else:
        correct_value = val
    return  correct_value

def process_child(each, elem_dict):             #Processing child elements such as "<tag>"
    key = each.get("k")
    params = key.split(":")                     # Check for "primary_key:secondary_key" patterns
    val = each.get("v")
    clean_output = cleaning_tech(key, val)
    if len(params) == 2 and type(elem_dict.get(params[0])) != str:  # Doesn't include fields which already are present as field: value. e.g name:en, name:af and "name"
        primary = params[0]
        secondary = params[1]
        if primary not in elem_dict:
            elem_dict[primary] = {}                             # Initializing field with primary key as empty dictionary, else KeyError exception is observed at primary_key
        elem_dict[primary][secondary] = clean_output

    elif len(params) == 1:
        if key in ["phone", "website"]:                         # Hard-coding for special keys
            if "contact" not in elem_dict:
                elem_dict["contact"] = {}
            elem_dict["contact"][key] = clean_output
        elif key in ["wikidata","wikipedia"]:
            if "wiki" not in elem_dict:
                elem_dict["wiki"] = {}
            elem_dict["wiki"][key] = clean_output
        else:
            elem_dict[key] = clean_output

    return elem_dict

# Main function run to clean the fields and shape the document
def clean_shape_data(filename):
    # Will return a list of dictionaries
    final_dict_list = []

    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "way":            # Each Node or Way as a dictionary of its child values
            elem_dict = {}
            elem_dict["creation_info"] = {}
            elem_dict["element_type"] = element.tag
            for att in INIT_INFO:
                if contains_attrib(att, element):
                    elem_dict[att] = element.attrib[att]

            for att1 in CREATED:
                if contains_attrib(att1, element):
                    elem_dict["creation_info"][att1] = element.attrib[att1]

            if contains_attrib("lon", element) and contains_attrib("lat", element):
                elem_dict["pos"] = [float(element.attrib["lat"]), float(element.attrib["lon"])]

            node_refs = []
            for child in element.iter("tag"):
                # send to process_child for evaluation
                if child.tag == "tag" and problemchars.search(child.attrib["k"]) is None:
                    elem_dict = process_child(child, elem_dict)
                if child.tag == "nd":
                    node_refs.append(child.attrib["ref"])
            final_dict_list.append(elem_dict)

    return  final_dict_list

# --**##### Cleaning algorithms end here #####**--


# Printing out cleaned data as JSON in filename.json
def process_map(file_in, pretty=False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        items_list = clean_shape_data(file_in)
        json.dump(items_list,fo)                            # Converting list of Dictionaries directly to JSON instead of writing to file again and again (as done in Course Exercises)
    return data

###################### END #########################

# UNCOMMENT THE FOLLOWING FILE WITH NAME OF FILE TO RUN THIS
##file_name = "delhi_map.osm"
##process_map(file_name)

