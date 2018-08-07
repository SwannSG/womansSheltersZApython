"""
    map wardId to municipality name

    input file: any ward geojson file
"""

import json
import pickle
import pprint

SRC_FILE = '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/merge/WCmerged.geojson'
PICKLE_FILE = '/home/swannsg/development/womansSheleterPy/data/sundryStuff/wardId_munName.pkl' 

fp = open(SRC_FILE, 'r')
x = json.load(fp)
fp.close()

fp = open(PICKLE_FILE, 'rb')
result = pickle.load(fp)
fp.close()

for each in x['features']:
    result[each['properties']['WardID']] = [ 
            each['properties']['Province'],
            each['properties']['MunicName'],
        ]

fp = open(PICKLE_FILE, 'wb')
pickle.dump(result,fp)
fp.close()

# pprint.pprint(result)
