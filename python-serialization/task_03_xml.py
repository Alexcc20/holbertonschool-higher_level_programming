#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to the given filename.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)
    print(f"Dictionary serialized to '{filename}'.")

def deserialize_from_xml(filename):
    """
    Reads XML data from a file and deserializes it into a Python dictionary.

    Parameters:
    filename (str): The filename to read the XML data from.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None
