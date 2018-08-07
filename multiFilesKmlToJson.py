"""
    convert multiple kml files to geojson format
    PROVINCE: set to the province eg. WC
    FILES_TO_IGNORE: files in SRC_DIR that should not be converted 
    SRC_DIR: contains multiple kml files
    DST_DIR: where kml to geojson result files are placed
"""
import os
import kmlToJson
import mergeGeoJsonFiles

# edit to process a province
PROVINCE = 'NW'
FILES_TO_IGNORE = ['EC.kml', 'FS.kml', 'KZN.kml', 'LIM.kml',
                   'MP.kml', 'NC.kml', 'NW.kml', 'WC.kml', 'KZN_KML_Files.zip']
# end edit to process a province

# edit for global dirs
SRC_DIR = '/home/swannsg/development/womansSheleterPy/data/kml'
DST_DIR = '/home/swannsg/development/womansSheleterPy/data/geoJson'
KML_TO_GEOJSON = True
MERGE_FILES = True
# end edit for global dirs

src_dir = SRC_DIR + '/' + PROVINCE
dst_dir = DST_DIR + '/' + PROVINCE

# create dirs if they don't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
# end create dirs if they don't exist

# get files and dirs in SRC_DIR
files_dirs = os.listdir(src_dir)

# remove names that are dirs from files_dirs
for each in files_dirs:
    if not os.path.isfile(src_dir + '/' + each):
        files_dirs.remove(each)

# remove filenames that are NOT to be processed
for each in files_dirs:
    try:
        if FILES_TO_IGNORE.index(each) >= 0:
            # filename must be removed
            files_dirs.remove(each)
    except:
        pass
    
# map kml files to geoJson
if KML_TO_GEOJSON:
    for each in files_dirs:
        print (src_dir + '/' + each, dst_dir)
        kmlToJson.runKmlToJson(src_dir + '/' + each, dst_dir)
# end map kml files to geoJson

# merge geoJson files
if MERGE_FILES:
    # ---get files and dirs in dst_dir
    files_dirs = os.listdir(dst_dir)
    # --remove names that are dirs from files_dirs
    for each in files_dirs:
        if not os.path.isfile(dst_dir + '/' + each):
            files_dirs.remove(each)

    # create dirs if they don't exist
    if not os.path.exists(DST_DIR + '/' + PROVINCE + '/merge'):
        os.makedirs(DST_DIR + '/' + PROVINCE + '/merge')
    # end create dirs if they don't exist

    mergeGeoJsonFiles.mergeGeoJsonFiles([dst_dir + '/' + a for a in files_dirs],
                                        dst_dir + '/merge/' + PROVINCE + 'merged.geojson')
# end merge geoJson files





