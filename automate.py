#!/usr/bin/python3
"""
    automate
        <arbitrary>
        topojson
        gzip
"""
import subprocess
import geoJsonAddPropName
import geoJsonChgPropName
import geoJsonDelPropName

DST_DIR = '/home/swannsg/development/womansSheleterPy/data/geoJson'
PROVINCES = ['EC', 'FS', 'KN', 'LIM', 'MP', 'NC', 'NW', 'WC']
PROVINCES = ['WC']

# CONFIG: add, chg, del feature properties as required
geoJsonAddPropName.PKL = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/female18-120.pkl'
geoJsonChgPropName.CHANGE_PROP_NAME = []
geoJsonDelPropName.DEL = []


for province in PROVINCES:
    fn_in = DST_DIR + '/' + province + '/merge/' + province + 'merged.geojson'
    fn_temp = DST_DIR + '/' + province + '/merge/' + province + 'merged.geojson' + '.bak'
    # backup the file
    subprocess.call(['cp', fn_in, fn_temp])
    print ('working with', fn_temp) 

    """
    # add, chg, del feature properties as required
    geoJsonChgPropName.SRC_FILE = fn_temp
    geoJsonDelPropName.SRC_FILE = fn_temp
    geoJsonAddPropName.SRC_FILE = fn_temp
    print ('chg properties')
    geoJsonChgPropName.chg()
    print ('delete properties')
    geoJsonDelPropName.delete()
    print ('add properties')
    geoJsonAddPropName.add()
    # end add, chg, del feature properties as required

    # topojson
    print ('topojson')
    subprocess.call(['rm', fn_temp + '.topojson'])
    cmd = 'geo2topo ' + fn_temp + ' > ' + fn_temp + '.topojson'
    print(subprocess.run(cmd, stdout=subprocess.PIPE, shell=True))
    """
    
    # gzip
    subprocess.run(['rm', fn_temp + '.topojson.zip'])
    subprocess.run(['zip', fn_temp + '.topojson.zip', fn_temp + '.topojson'])


    
