import requests
import json 
# https://covid-api.com/api/regions?per_page=20

with requests.get("https://covid-api.com/api/regions") as r:
    data=json.loads(r.text)
    with open("dummy_cvd_data.txt",'w') as w:
            print(json.dump(data,w,indent=2))

# json.load() → Read JSON data from a file and convert it into a Python object.

# json.loads() → Read JSON data from a string and convert it into a Python object.


