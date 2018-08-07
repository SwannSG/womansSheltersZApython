"""
    Statistics South Africa
    Descriptive_Electoral_Wards
    Table 1
    Geography by Gender
     for Person weighted
    ,"Male","Female","Grand Total"
    "21001001: Ward 1",4242,4500,8742

    National data is mapped to hash map (dict) called 'result'
        key: value
        wardId: #females
        21001001: 4500

    'result' is pickled
"""
import pickle
filename = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/South African population data by most detailed wards and gender.csv'

pkl = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/wardPop.pkl'
result = {}
start = False
fp = open(filename, 'r')
i = 0
for each in fp:
   # print (i)
    if each == ',"Male","Female","Grand Total"\n':
        start = True
        continue
    if start:
        a,b,c,d = each.split(',')
        if a == '"Grand Total"':
            break
        a = a.replace('"', '')
        result[a.split(':')[0]] = int(c)
    i = i + 1

fp.close()
fp = open(pkl, 'wb')
pickle.dump(result, fp)
fp.close()


    
