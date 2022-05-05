import sys, csv, gzip, pickle
from collections import defaultdict, Counter
from pprint import pprint
import numpy as np
DATA_DIR = '../data/'

# min, avg, max
WEIGHT_RENS = [1, 7/4, 2]
WEIGHT_ISOLARIO = [0, 7/4, 3]
WEIGHT_STATE_OWNED = [-2, -1, 0]
WEIGHT_POC = [-2, 3/4, 3]
WEIGHT_PERSONALUSE = [0, 2, 3]
WEIGHT_COMMPROJ = [0, 3/4, 2]

# gov harder (-1) compared to education
# security companies harder (-1) compared to cloud provider
# CDN much harder (-2) compared to anycast DNS
# emerging regions are harder to peer with in general
# interestingly, all asdb classes got 'no influence' as majority

def collapse_weights(weights_per_asn, ctype):
    collapsed = defaultdict(int)
    for asn, weights in weights_per_asn.items():
        minw, maxw = min(weights), max(weights)
        if ctype == 0:
            collapsed[asn] = minw/3.0

        if ctype == 1:
            collapsed[asn] = maxw/3.0

        if ctype == 2:
            if minw == -3:
                collapsed[asn] = -1.0
                continue

            if maxw == 3:
                collapsed[asn] = 1.0
                continue

            collapsed[asn] = np.mean(weights)/3.0
    return collapsed

def pairwise(iterable):
    a = iter(iterable)
    return set(zip(a, a))

def boostrap_naics_weights(which):
    # quick and dirty, don't judge me ...
    sys.path.append(DATA_DIR+'asdb/')
    from naics_weights import NAICS_WEIGHTS
    print(f'Number of unique NAICS labels: {len(NAICS_WEIGHTS)}')

    weights_per_asn = defaultdict(list)
    filename = DATA_DIR+'asdb/asdb_snapshot_20220202.csv'
    with open(filename, 'rt') as ifile:
        csv_reader = csv.reader(ifile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
            if i == 0: continue

            # parse line
            ASN, categories = row[0], row[1:]
            if not ASN.startswith('AS') or not ASN[2:].strip().isnumeric():
                print('### Error when parsing ASN, problematic line:\n %s' %(row))
                continue

            for cat, sub in pairwise(categories):
                # ignore broken records
                if len(cat.strip()) == 0: continue
                if len(sub.strip()) == 0: continue

                label = f'{cat} -> {sub}'
                if not label in NAICS_WEIGHTS: continue
                weights_per_asn[ASN].append(NAICS_WEIGHTS.get(label, [0, 0, 0])[which])

    return weights_per_asn

def add_isolario_weights(weights_per_asn, which):
    filename = DATA_DIR + 'isolario/peer_asns_all.txt'
    with open(filename) as ifile:
        for line in ifile:
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_ISOLARIO[which])

def add_state_owned_weights(weights_per_asn, which):
    filename = DATA_DIR + 'state-owned/state_owned_ases.csv'
    with open(filename, 'rt') as ifile:
        csv_reader = csv.reader(ifile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
            if i == 0: continue
            weights_per_asn[f'AS{row[0].rstrip()}'].append(WEIGHT_STATE_OWNED[which])

def add_nren_weights(weights_per_asn, which):
    filename = DATA_DIR + 'rens/rens_europe.csv'
    with open(filename, 'rt') as ifile:
        csv_reader = csv.reader(ifile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
            if i == 0: continue
            weights_per_asn[f'AS{row[2].rstrip()}'].append(WEIGHT_RENS[which])

def add_positive_openess_weights(weights_per_asn, which):
    filename = DATA_DIR + 'data-openess/openess_positive_asns.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_OPENESS[which])

def add_negative_openess_weights(weights_per_asn, which):
    filename = DATA_DIR + 'data-openess/openess_negative_asns.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(-1*WEIGHT_OPENESS[which])

def add_personaluse_weights(weights_per_asn, which):
    filename = DATA_DIR + 'personal-use/personel-use-asns.csv'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_PERSONALUSE[which])

def add_commproj_weights(weights_per_asn, which):
    filename = DATA_DIR + 'project_peers/community_project_members.csv'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_COMMPROJ[which])

def add_poc_weights(weights_per_asn, which):
    filename = DATA_DIR + 'poc/peeringdb/asns_with_pdb_poc.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_POC[which])


def show_weight_distribution(weights_per_asn):
    c = Counter(weights_per_asn.values())
    print('# summed weight: number of ASNs with that weight')
    for i in sorted(c):
        print(f'{i}: {c[i]}')


def produce_run(which, ctype):
    wnames = ['min', 'avg', 'max']
    cnames = ['min', 'max', 'merge']
    weights_per_asn = boostrap_naics_weights(which)

    add_state_owned_weights(weights_per_asn, which)
    #add_positive_openess_weights(weights_per_asn)
    #add_negative_openess_weights(weights_per_asn)
    add_personaluse_weights(weights_per_asn, which)
    add_isolario_weights(weights_per_asn, which)
    add_nren_weights(weights_per_asn, which)
    add_commproj_weights(weights_per_asn, which)

    final_weights = collapse_weights(weights_per_asn, ctype)
    with gzip.open(f'final_weights/weighs_{wnames[which]}_{cnames[ctype]}.pkl.gz', 'wb') as out:
        pickle.dump(final_weights, out)


for which in range(3):
    for ctype in range(3):
        produce_run(which, ctype)

