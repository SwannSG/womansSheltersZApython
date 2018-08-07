"""
    geoJsonChgPropName.py

    Change the the name of the property

    feature.properties = {key_1: value_1, ...}
    Change key_oldName to key_newName, keeping value the same
        An existing key_newName value will be overwritten 

    CHANGE_PROP_NAME = [(oldName, newName), ...]
"""
import json
import pickle
import pprint

SRC_FILE = '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/merge/WCmergedTest.geojson'

CHANGE_PROP_NAME = [('Province', 'Pr'), ('MunicName', 'Mn')]

def chg():
    fp = open(SRC_FILE, 'r')
    x = json.load(fp)
    fp.close()


    # change property name
    for feature in x['features']:
        for keyOld, keyNew in CHANGE_PROP_NAME:
            if keyOld in feature['properties']:
                value = feature['properties'][keyOld]
                feature['properties'].pop(keyOld, None)
                feature['properties'][keyNew] = value
                

    # show result
    #for each in x['features']:
    #    pprint.pprint(each['properties'])

    fp = open(SRC_FILE, 'w')
    json.dump(x, fp)
    fp.close()
