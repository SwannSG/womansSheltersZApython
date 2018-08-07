"""
    geoJsonDelPropName.py

    feature.properties = {key_1: value_1, ...}
    Delete key_N from feature.properties
"""

import json
import pickle
import pprint

SRC_FILE = '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/merge/WCmergedTest.geojson'
DEL = ['females']

def delete():
    fp = open(SRC_FILE, 'r')
    x = json.load(fp)
    fp.close()


    # del properties
    for feature in x['features']:
        for each in DEL:
            feature['properties'].pop(each, None)

    # show result
    #for each in x['features']:
    #    pprint.pprint(each['properties'])

    fp = open(SRC_FILE, 'w')
    json.dump(x, fp)
    fp.close()
