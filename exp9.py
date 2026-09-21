import csv
import json

# Define file paths
input_file = "input.csv"
output_file = "output.json"

# Open and read the CSV file
with open(input_file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write data to JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")