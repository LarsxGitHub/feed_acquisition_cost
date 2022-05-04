import json, sys

with open(sys.argv[1], 'rt') as ifile:
    data = json.load(ifile)

accepted_roles = {
    'Maintenance',
    'NOC',
    'Policy',
    'Technical'}

netids = set()
for poc in data['poc']['data']:
    if poc['role'] not in accepted_roles: continue
    if len(poc['role'].strip()) == 0: continue
    if len(poc['email'].strip()) == 0: continue
    netids.add(poc['net_id'])

asns = set()
for net in data['net']['data']:
    if not net['id'] in netids: continue
    asns.add(int(net['asn']))

for asn in sorted(asns):
    print(asn)
