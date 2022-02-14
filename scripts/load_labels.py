import sys, csv
from collections import defaultdict, Counter
from pprint import pprint
from statistics import harmonic_mean as hmean

DATA_DIR = '../data/'

WEIGHT_RENS = 2
WEIGHT_ISOLARIO = 3
WEIGHT_STATE_OWNED = -1

def collapse_weights(weights_per_asn):
    collapsed = defaultdict(int)
    for asn, weights in weights_per_asn.items():
        offset = -1*min(weights)+1
        non_zero = [x+(offset) for x in weights if x != 0]
        if not non_zero:
            collapsed[asn] = 0
            continue

        collapsed[asn] = hmean(non_zero)-(offset)
    return collapsed

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

def boostrap_naics_weights():
    # quick and dirty, don't judge me ...
    sys.path.append(DATA_DIR+'asdb/')
    from naics_weights import NAICS_WEIGHTS

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

def show_weight_distribution(weights_per_asn):
    c = Counter(weights_per_asn.values())
    print('# summed weight: number of ASNs with that weight')
    for i in sorted(c):
        print(f'{i}: {c[i]}')

weights_per_asn = boostrap_naics_weights()
add_state_owned_weights(weights_per_asn)
add_isolario_weights(weights_per_asn)
add_nren_weights(weights_per_asn)

final_weights = collapse_weights(weights_per_asn)
show_weight_distribution(final_weights)
