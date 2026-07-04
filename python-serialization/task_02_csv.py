#!/usr/bin/env python3
"""Convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json and report whether it succeeded."""
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except (OSError, csv.Error):
        return False
