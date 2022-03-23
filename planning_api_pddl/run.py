import sys, json
from urllib import parse, request

data = {'domain': open(sys.argv[1], 'r').read(), 'problem': open(sys.argv[2], 'r').read()}
response = {}
while not response or response['result'] == 'Server busy...':
    try:
        response = json.loads(request.urlopen(request.Request('http://solver.planning.domains/solve', data=parse.urlencode(data).encode('utf-8'))).read())
    except:
        pass

if response:
    verbose = len(sys.argv) > 3 and sys.argv[3] == '-v'
    print(response['status'])
    if response['status'] != 'ok':
        if verbose and 'error' in response['result']:
            print(response['result']['error'])
        elif 'output' in response['result']:
            print(response['result']['output'])
    elif verbose:
        print('\n'.join(step['name'] for step in response['result']['plan']))
    with open(f"{sys.argv[2].rpartition('.')[0]}_results.json", 'w') as outfile:
        json.dump(response, outfile, indent=2)
else:
    print('error')

