# Java script object notation
import json
import pandas

#load json file to a python object and viceversa

with open('states.json','r') as f:
    data=json.load(f)
    for keys in data['states']:
        del keys['region']

    with open('new_state.json','w') as f:
            json.dump(data,f,indent=2)
    