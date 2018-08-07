"""
    Merge ZA ward geoJson files into one output file

"""
import pprint
import json

# global settings
    # ---temporary working directory
TEMP_WDIR = '/home/swannsg/development/womansSheleterPy/temp'
DST_FILENAME = 'merge.geojson'
# end global settings

srcFiles = [
    '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/WC021.geojson',
    '/home/swannsg/development/womansSheleterPy/data/geoJson/WC/WC052.geojson'
    ]


def mergeGeoJsonFiles(srcFiles, dstFile=TEMP_WDIR + '/' + DST_FILENAME):
    """
        srcFiles: list of fq filenames to merge
        dstFile: where the output file must be placed
    """
    pprint.pprint(srcFiles)
#    pprint.pprint(dstFile)


    result = {}
    result['type'] = 'FeatureCollection'
    result['name'] = ''
    result['features'] = []
    for each in srcFiles:
        fp = open(each, 'r')
        x = json.load(fp)
        fp.close()
        result['name'] = result['name']  + ' ' + x['name']
        result['features'] = result['features'] + x['features'] 
    result['name'].strip()

    # dict 'result' to json
    fp = open(dstFile, 'w')
    json.dump(result, fp)
    fp.close()
    # end dict 'result' to json
