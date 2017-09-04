#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
import xml.etree.ElementTree as ET  # Use cElementTree or lxml if too slow

OSM_FILE = "delhi_map.osm"  # Replace this with your osm file
SAMPLE_FILE = "sample_data_submission.osm"


def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag

    Reference:
    http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    """
    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


with open(SAMPLE_FILE, 'wb') as output:
    output.write(bytes('<?xml version="1.0" encoding="UTF-8"?>\n', 'UTF-8'))
    output.write(bytes('<osm>\n  ', 'UTF-8'))

    # Write every kth top level element
    k = 50
    for i, element in enumerate(get_element(OSM_FILE)):
        if i % k == 0:
            output.write(ET.tostring(element, encoding='utf-8'))

    output.write(bytes('</osm>', 'UTF-8'))