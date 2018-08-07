"""
    geoJsonAddPropName.py

    feature.properties = {key_1: value_1, ...}
        add new properties {key_N: value_N} for wardId=NNNNNNN
    feature.properties = {key_1: value_1, ..., key_N: value:N}

    ADD_PROP = {wardId: {key_1: value_1, ...}
        additional key-value pairs will be added to
        feature.properties where feature.properties.wardId = wardId 
"""

import json
import pickle
import pprint

SRC_FILE = '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/merge/WCmergedTest.geojson'
PKL = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/female18-120.pkl'


def add():
    fp = open(PKL, 'rb')
    ADD_PROP = pickle.load(fp)  
    fp.close()

    fp = open(SRC_FILE, 'r')
    x = json.load(fp)
    fp.close()


    # del properties
    for feature in x['features']:
        feature_properties = feature['properties']
        ward_id = feature_properties['WardID']
        if ward_id in ADD_PROP:
            feature_properties.update(ADD_PROP[ward_id])
            feature['properties'] = feature_properties 
            
    # show result
    #for each in x['features']:
    #    pprint.pprint(each['properties'])

    fp = open(SRC_FILE, 'w')
    json.dump(x, fp)
    fp.close()
    
