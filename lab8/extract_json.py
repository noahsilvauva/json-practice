#!/usr/bin/env python3

import json
import csv

with open('data/schacon.repos.json', 'r') as file_json:
    data = json.load(file_json)

with open('lab8/chacon.csv', 'w', newline='') as file_csv:
    writer = csv.writer(file_csv)
    for d in range(5):
        chacon_newline = [data[d]['name'],data[d]['html_url'],data[d]['updated_at'],data[d]['visibility']]
        writer.writerow(chacon_newline)

# Sources:

# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/
# https://stackoverflow.com/questions/1938227/int-object-is-not-iterable-while-trying-to-sum-the-digits-of-a-number
# https://stackoverflow.com/questions/58192471/csv-writer-inserting-comma-between-each-character