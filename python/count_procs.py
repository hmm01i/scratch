import os
import resource

pids = (p for p in os.listdir('/proc') if p.isdigit())
c = 0
for p in pids:
  c += 1

print(c)
print
print(resource.getrusage(resource.RUSAGE_SELF))

del pids,c

pidls = [p for p in os.listdir('/proc') if p.isdigit()]
print(len(pidls))

print
print(resource.getrusage(resource.RUSAGE_SELF))

