import csv
import json
from os import replace

def parse_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def convert_to_json(parsed_data):
    # Convert the parsed data to JSON string with pretty printing
    return json.dumps(parsed_data, indent=2)


# Example usage
# csv_file = "../datasets/dataset2.csv"  # Replace with your actual CSV file
# parsed_data = parse_csv(csv_file)
# json_data = convert_to_json(parsed_data)
# print(json_data)
