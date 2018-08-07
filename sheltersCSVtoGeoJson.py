"""
    shelters.csv to geoJson
"""
import pprint
import json

CSV = '/home/swannsg/development/womansSheleterPy/data/sheltersFromKirsty/Western Cape Shelters GPS coordinates.csv'
OUT = '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/shelters/WCshelters.geojson'

result= {}
result['type'] = 'FeatureCollection'
result['name'] = 'WC Shelters'
result['features'] = []


fp = open(CSV, 'r')

for i, each in enumerate(fp):
    if i == 0:
        # ignore first line
        continue
    each.replace('\n', '')
    area, name, lat, lng, num = each.split(',')
    # init feature
    feature = {'type':'Feature',
           'geometry': {'coordinates': [], "type": 'Point'},
           'properties': {'area': '', 'name': ''}}

    # set values in feature
    feature['geometry']['coordinates'] = [float(lng.replace('"', '')),
                                          float(lat.replace('"', ''))]
    feature['properties']['area'] = area
    feature['properties']['name'] = name

    # add to features
    result['features'].append(feature)
fp.close()

fp = open(OUT, 'w')
json.dump(result, fp)
fp.close()

