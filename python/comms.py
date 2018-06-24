import os

pids = [p for p in os.listdir('/proc') if p.isdigit()]
comm = [open('/proc/'+p+'/comm').read().rstrip('\n') for p in pids]
print(comm)

print(len(comm))
