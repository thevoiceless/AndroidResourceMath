#! /usr/bin/env python

import xml.etree.ElementTree as ET
import re

tree = ET.parse('test.xml')
root = tree.getroot()

evaluated_dimens = {}

def do_math(child):
    print "Doing math on", child.text
    values = re.findall('([0-9]?\.?[0-9]+)(dp|sp|px)?', child.text)
    print "do_math", values
    # TODO: For now assume units exist and match
    unit = values[0][1]
    for value in values:
        print "Replacing", value[0] + value[1], "with", value[0]
        child.text = child.text.replace(value[0] + value[1], value[0])
    print "Evaluating:", child.text, "=", str(eval(child.text)) + unit
    child.text = str(eval(child.text)) + unit

# Dimens
for child in root.iter('dimen'):
    print child.tag, child.attrib, child.text
    dimen_name = child.attrib['name']
    dimen_refs = re.findall('(@dimen/)([a-z_]+)', child.text)
    if len(dimen_refs) > 0:
        print "Evaluate", dimen_name, "=", child.text
        for pair in dimen_refs:
            replace_text = pair[0] + pair[1]
            print "Replacing", replace_text, "with", evaluated_dimens[pair[1]]
            child.text = child.text.replace(replace_text, evaluated_dimens[pair[1]])
        do_math(child)
    evaluated_dimens[dimen_name] = child.text

tree.write('out.xml')
