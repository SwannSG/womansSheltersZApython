"""
    Statistics South Africa
    Descriptive_Electoral_Wards
    Table 1
    Geography by Gender
    " for Person weighted, 18 - 120"
    ,"Male","Female","Grand Total"

    Females 18 to 120

    output = {wardID: {f18-120: <number>}}
    result is pickled
"""
import pickle
filename = "/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/sourceData/Whole of SA women's population 18 and upwards - most detailed with codes no names.csv"
pkl = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/female18-120.pkl'
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
        result[a.split(':')[0]] = {'f18-20': int(c)}
    i = i + 1

fp.close()
fp = open(pkl, 'wb')
pickle.dump(result, fp)
fp.close()
