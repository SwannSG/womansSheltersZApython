"""
    kml to geojson
    shapefiles WC
        handles all files
        does not handle WC.kml format ????

    Read population statistics at the same time
        feature.properties.woman = #woman
        see wardPopulation.py

    Still needed/ to be checked:
        can we minimise the file further eg. drop 3rd coord

    Questions
        do we merge all these files into one provincial file,
        or national file ?
        missing female populations for certain wardIds - why ?

"""
import kml2geojson as kml
import json
from bs4 import BeautifulSoup as bs
import pickle
import os
import ntpath

# global settings
    # ---temporary working directory
temp_wdir = '/home/swannsg/development/womansSheleterPy/temp'
    # ---used to merge population data feature.properties.females
PKL = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/wardPop.pkl'
    #---wardIds missing female population (MFP) 
MFP = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/mfp.pkl'
# end global settings

# load female population
fp = open(PKL, 'rb')
females = pickle.load(fp)
fp.close()
# end load female population

# load wardIds with missing female population
if os.path.isfile(MFP):
    # mssing female population pickle file exists
    fp = open(MFP, 'rb')
    mfp = pickle.load(fp)
    fp.close()
else:
    mfp = []
# end load wardIds with missing female population

def parse_update(descHTML, ref): 
    soup = bs(descHTML, 'html.parser')
    for each in soup.findAll('tr'):
        key, value = each.text.split(':')
        ref[key] = value


def runKmlToJson(srcFile, dstDir):
    # the arguments are a bit confusing
    #---- srcFile:  input file to process
    #---- dstDir:final destination dir, "dst_dir"

    # convert to GeoJSON
    kml.main.convert(srcFile, temp_wdir)
    # kml seems to automatically generate a filename
    # ----<srcFile filename without extension>.geojson
    # infer destination filename
    infer_filename = ntpath.basename(srcFile).split('.')[0] + '.geojson'
    print (infer_filename)
    # read geojson file
    fp = open(temp_wdir + '/' + infer_filename)
    x = json.load(fp)
    fp.close()
    # delete interim geojson file
    os.remove(temp_wdir + '/' + infer_filename)
    

    # clean & minimise geojson file
    result = {}
    result['type'] = x['type']
    result['features'] = []
    result['name'] = x['name']

    i = 0
    for each in x['features']:
            # print (i)
            # initialise feature
            feature = {}
            feature['type'] = each['type'] 
            feature['geometry'] = {}
            feature['properties'] = {}
            # end initialise feature

            # add feature props and values
            feature['properties']['name'] =  each['properties']['name']
            parse_update(each['properties']['description'], feature['properties'])
            if each['geometry']['type'] == 'GeometryCollection':
                feature['geometry']['type'] = each['geometry']['type']
                feature['geometry']['geometries'] = each['geometry']['geometries'] 
            else:
                feature['geometry']['coordinates'] = each['geometry']['coordinates'] # clean 3rd point !!!!!!
                feature['geometry']['type'] = each['geometry']['type']
            # end add feature props and values

            # remove feature.properties.<key> that are not required   
            DEL_KEYS = ['CAT_B', 'MapCode', 'OBJECTID', 'Shape_Area', 'Shape_Leng', 'WardNo', 'name', 'shpFID']
            for item in DEL_KEYS:
                del feature['properties'][item]
            # end remove feature.properties.<key> that are not required   
            
            # add external feature.properties.females
                # we probably need a generic property add approach !!!!
                if feature['properties']['WardID'] in females:
                    feature['properties']['females'] = females[feature['properties']['WardID']]
                else:
                    # don't add duplicates
                    try:
                        if mfp.index(feature['properties']['WardID']) > -1:
                            # wardId exists, do nothing
                            pass
                    except:
                        # new wardId so add it to "mfp"
                        mfp.append(feature['properties']['WardID'])

                    # WARNING !!!! arbitrarily sets feature.properties.females to zero
                    feature['properties']['females'] = 0
            # end add external feature.properties.females

            # only add geometry.type = 'Polygon'
            if feature['geometry']['type'] ==  'Polygon' or \
               feature['geometry']['type'] ==  'GeometryCollection':
                result['features'].append(feature)
            i = i + 1   

    # dict 'result' to json
    fp = open(dstDir + '/' + result['name'] + '.geojson', 'w')
    json.dump(result, fp)
    fp.close()
    # end dict 'result' to json


    # pickle missing_female_population
    fp = open(MFP, 'wb')
    pickle.dump(mfp, fp)
    fp.close()
    # end pickle missing_female_population


