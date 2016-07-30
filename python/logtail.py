import os,sys,subprocess
import json


filename = sys.argv[1]
string = sys.argv[2]
file_pos = filename+'.pos'
with open(file_pos,'r') as p:
	pos = p.readline().rstrip('\n')

if pos.isdigit():
	print('starting position: '+pos)
	pos = int(pos)
else:
	print("it's not a digit")
	exit(1)

with open(filename,'r') as f:
	f.seek(pos)
	lines = [l for l in f]
	new_pos = str(f.tell())


print(lines)
print('new position: ' + new_pos)
with open(file_pos,'w') as p:
	p.write(new_pos)
	p.flush()
	os.fsync(p.fileno())
