"""
PROGRAM TO CREATE A DICTIONARY OF THE CSV FILE
"""

import os, csv, json

current_path = os.getcwd() + '/dictionary_converter'
with open(current_path + '/dict.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader if not ('' in row.values())]
with open(current_path + '/dict.json', 'w') as json_file:
    json.dump(data, json_file)