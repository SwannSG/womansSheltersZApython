"""
    View missing female populations for specific wardId
"""
import pprint
import pickle

MFP = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/mfp.pkl'

fp = open(MFP, 'rb')
mfp = pickle.load(fp)
fp.close()

pprint.pprint(mfp)

