import os
import resource

pidls = [p for p in os.listdir('/proc') if p.isdigit()]
print(len(pidls))

print
print(resource.getrusage(resource.RUSAGE_SELF))

