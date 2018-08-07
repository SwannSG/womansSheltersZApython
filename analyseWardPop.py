"""
    analyse ward population
"""
import pprint
import pickle


file = '/home/swannsg/development/womansSheleterPy/data/femalePopulationFromKirsty/wardPop.pkl'
fp = open(file, 'rb')
wardPops = pickle.load(fp)
fp.close()

l = []
for each in wardPops:
    l.append(int(wardPops[each]))

l.sort()
# pprint.pprint(l)

a = 0
b = 0
c = 0
d = 0
e = 0
bin_size = 3500 # bad
bin_size = 2000 # ok
#bin_size = 2500
bins = []
for each in l:
    if each > bin_size * 4:
        e  = e + 1
        continue
    if each > bin_size * 3:
        d  = d + 1
        continue
    if each > bin_size * 2:
        c  = c + 1
        continue
    if each > bin_size * 1:
        b  = b + 1
        continue
    a = a + 1

print (a,b,c,d,e)



