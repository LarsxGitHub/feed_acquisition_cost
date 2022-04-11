import sys, csv, gzip, pickle
from collections import defaultdict, Counter
from pprint import pprint
import numpy as np
DATA_DIR = '../data/'

WEIGHT_RENS = 2
WEIGHT_ISOLARIO = 2
WEIGHT_STATE_OWNED = -1
WEIGHT_PRIVATE = 3
WEIGHT_OPENESS = 1
WEIGHT_POC = 2
WEIGHT_PERSONALUSE = 1
WEIGHT_ANYCAST = 1

# gov harder (-1) compared to education
# security companies harder (-1) compared to cloud provider
# CDN much harder (-2) compared to anycast DNS
# emerging regions are harder to peer with in general
# interestingly, all asdb classes got 'no influence' as majority

def collapse_weights(weights_per_asn):
    collapsed = defaultdict(int)
    for asn, weights in weights_per_asn.items():
        minw, maxw = min(weights), max(weights)
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

def boostrap_naics_weights():
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
                weights_per_asn[ASN].append(NAICS_WEIGHTS.get(label, 0))

    return weights_per_asn

def add_isolario_weights(weights_per_asn):
    filename = DATA_DIR + 'isolario/peer_asns_all.txt'
    with open(filename) as ifile:
        for line in ifile:
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_ISOLARIO)

def add_state_owned_weights(weights_per_asn):
    filename = DATA_DIR + 'state-owned/state_owned_ases.csv'
    with open(filename, 'rt') as ifile:
        csv_reader = csv.reader(ifile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
            if i == 0: continue
            weights_per_asn[f'AS{row[0].rstrip()}'].append(WEIGHT_STATE_OWNED)

def add_nren_weights(weights_per_asn):
    filename = DATA_DIR + 'rens/rens_europe.csv'
    with open(filename, 'rt') as ifile:
        csv_reader = csv.reader(ifile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
            if i == 0: continue
            weights_per_asn[f'AS{row[2].rstrip()}'].append(WEIGHT_RENS)

def add_positive_openess_weights(weights_per_asn):
    filename = DATA_DIR + 'data-openess/openess_positive_asns.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_OPENESS)

def add_negative_openess_weights(weights_per_asn):
    filename = DATA_DIR + 'data-openess/openess_negative_asns.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(-1*WEIGHT_OPENESS)

def add_personaluse_weights(weights_per_asn):
    filename = DATA_DIR + 'personal-use/personel-use-asns.csv'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_PERSONALUSE)

def add_anycast_weights(weights_per_asn):
    filename = DATA_DIR + 'anycast/anycast_asns_all.csv'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_ANYCAST)

def add_poc_weights(weights_per_asn):
    filename = DATA_DIR + 'poc/peeringdb/asns_with_pdb_poc.txt'
    with open(filename, 'rt') as ifile:
        for line in ifile:
            if not line.strip(): continue
            weights_per_asn[f'AS{line.rstrip()}'].append(WEIGHT_POC)


def show_weight_distribution(weights_per_asn):
    c = Counter(weights_per_asn.values())
    print('# summed weight: number of ASNs with that weight')
    for i in sorted(c):
        print(f'{i}: {c[i]}')


weights_per_asn = boostrap_naics_weights()
add_state_owned_weights(weights_per_asn)
add_positive_openess_weights(weights_per_asn)
add_negative_openess_weights(weights_per_asn)
add_personaluse_weights(weights_per_asn)
add_isolario_weights(weights_per_asn)
add_nren_weights(weights_per_asn)
add_anycast_weights(weights_per_asn)

final_weights = collapse_weights(weights_per_asn)
# show_weight_distribution(final_weights)
with gzip.open('weighs_per_asn.pkl.gz', 'wb') as out:
    pickle.dump(final_weights, out)

