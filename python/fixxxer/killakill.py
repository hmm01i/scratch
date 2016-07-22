import os

#we need to take an arg for process name

cmd = ''
pids = [pid for pid in os.listdir('/proc/') if pid.isdigit()]

op = open.os
for p in pids:
  if open('/proc/'+p+'/comm).readline().rstrip() == cmd:
    try:
      os.kill(int(p),15)
    except:
      print('it might not be there anymore')
