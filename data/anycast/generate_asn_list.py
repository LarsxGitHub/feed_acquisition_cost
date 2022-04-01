import sys, json, gzip
from pytricia import PyTricia
P2AS_FILE=sys.argv[1]
M2_FILE=sys.argv[2]


def is_reserved(asn):
    asn = int(asn)
    if asn == 0: return True
    if asn == 112: return True
    if asn == 23456: return True
    if 64496 <= asn <= 65556: return True
    if 401309 < asn: return True
    return False


pyt = PyTricia()
with gzip.open(P2AS_FILE, 'rt') as ifile:
    for line in ifile:
        base, cidr, asn = line.split()
        try:
             asn = int(asn)
             if is_reserved(asn): continue
             cidr = int(cidr)
             #if cidr <24: continue
             pyt[f'{base}/{cidr}'] = asn
        except:
             # 80 covering/as-set prefixes
             continue

asns = set()
with open(M2_FILE) as ifile:
    for line in ifile:
        data = json.loads(line)
        asn = pyt.get(data['ip4_prefix']+'/24')
        if asn:
            asns.add(asn)

for asn in sorted(asns):
    print(asn)
