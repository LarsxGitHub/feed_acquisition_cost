import requests
URL='https://asdb.stanford.edu/NAICSlite.csv'

with requests.Session() as s, open('naics_weights.py', 'w+') as out:
    content = s.get(URL).content.decode('utf-8')
    layer_twos = []
    maincat = ''
    out.write('NAICS_WEIGHTS = {\n')
    for i, line in enumerate(content.splitlines()):
        if i == 0: continue
        cat, layer = line.rsplit(',', 1)
        if int(layer) == 2:
            layer_twos.append(cat)
        else:
            for subcat in layer_twos:
                out.write(f'    \'{maincat} -> {subcat}\': '.ljust(150)+f'0,'.rjust(3)+'\n')
            maincat = cat
            layer_twos = []
    out.write(f'    \'Unknown -> Unknown\':'.ljust(150)+f'0 '.rjust(3)+'\n')
    out.write('}\n')
