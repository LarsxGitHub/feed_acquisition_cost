import sys, json, pickle

DUMP_FN = '../../results/data-openess/openness_vals.pkl'

with open(sys.argv[1]) as ifile:
    data = json.load(ifile)

vals = []
for elem in data:
    vals.append(elem["OpennessScore"])

vals = sorted(vals)
with open(DUMP_FN, 'wb') as out:
    pickle.dump(vals, out)
