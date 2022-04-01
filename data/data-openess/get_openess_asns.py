import sys, json, pickle
import os
from smart_open import open
from collections import defaultdict
import pycountry

OUT_PLUS = 'openess_positive_asns.txt'
OUT_MINUS = 'openess_negative_asns.txt'

DIR = './deleg_files/'

def yield_asn_cc_paris():
    for fn in os.listdir(DIR):
        with open(os.path.join(DIR, fn), 'rt') as ifile:
            for line in ifile:
                 elems = line.split('|')
                 if len(line) == 0 or elems[0][0].isdigit() or elems[0].startswith('#') or len(elems) == 6:
                     continue
                 registry, cc, rtype, start, value, date, status, *extra = elems
                 if rtype.strip() != 'asn': continue
                 if not cc.strip(): continue
                 for i in range(int(value)):
                     yield int(start)+i, cc.strip()

def load_scores():
    with open(sys.argv[1]) as ifile:
        data = json.load(ifile)

    scores = dict()
    for elem in data:
        scores[elem['CountryCode']] = float(elem["OpennessScore"])
    return scores

def save_to_file(fn, asns):
    with open(fn, 'wt') as out:
        for asn in asns:
            out.write(str(asn)+'\n')

tlower, tupper = 30.0, 87.0
asns_neg, asns_pos = [], []
scores = load_scores()
for asn, cc in yield_asn_cc_paris():
    # convert cc formats
    try:
        cc3 = pycountry.countries.get(alpha_2=cc).alpha_3
    except AttributeError:
        continue
    score = scores.get(cc3, None)
    if not score: continue
    if score < tlower:
        asns_neg.append(asn)
    elif score > tupper:
        asns_pos.append(asn)

save_to_file(OUT_MINUS, asns_neg)
save_to_file(OUT_PLUS, asns_pos)
