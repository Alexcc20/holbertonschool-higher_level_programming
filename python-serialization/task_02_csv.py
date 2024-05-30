#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and writes it to data.json.

    Parameters:
    csv_filename (str): The filename of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Read CSV file and convert to a list of dictionaries
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Write the list of dictionaries to a JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
