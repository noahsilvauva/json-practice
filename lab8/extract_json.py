#!/usr/bin/env python3

import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

data[0]

#for d in data_json[0]: 
#    print(d["name"]) 

#name
#html_url
#updated_at
#visibility