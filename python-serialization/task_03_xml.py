#!/usr/bin/env python3
"""Serialize dictionaries to XML and deserialize XML back to dictionaries."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
