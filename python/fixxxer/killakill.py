import os,sys

#we need to take an arg for process name
cmd = sys.argv[1]
pids = [pid for pid in os.listdir('/proc/') if pid.isdigit()]

ok = os.kill
for p in pids:
  if open('/proc/'+p+'/comm).readline().rstrip() == cmd:
    try:
      ok(int(p),15)
    except:
      print('it might not be there anymore')
