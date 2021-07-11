import csv
import os

file_to_load = os.path.join("election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

