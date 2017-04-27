import json

stats = {}

def increment(stat, increase=1):
    try:
        stats[stat] += increase
    except KeyError:
        stats[stat] = increase

def gauge(stat, value=''):
        status[stat] = value

def storeStats(file):
    print(json.dumps(stats))
    with open(file,'w') as f:
        json.dump(stats,f)

