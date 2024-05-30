#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
    data (dict): A Python dictionary with data.
    filename (str): The filename of the output JSON file. If the output file already exists, it should be replaced.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    print(f"Data deserialized from '{filename}'.")
    return data
