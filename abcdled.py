import time
import commands
from subprocess import Popen

while True:
  t_fb = commands.getstatusoutput('ps -eo pid,args | grep script3.py | grep -v service | grep -v init.d | grep -v grep | cut -c1-6')
  t_ph = commands.getstatusoutput('ps -eo pid,args | grep script1.py | grep -v service | grep -v init.d | grep -v grep | cut -c1-6')
  t_fb = commands.getstatusoutput('ps -eo pid,args | grep script2.py | grep -v service | grep -v init.d | grep -v grep | cut -c1-6')
  if t_fb[1] == '':
    r_fb = Popen(["bash", "script3.sh"])
  if t_ph[1] == '':
    r_ph = Popen(["bash", "script1.sh"])
  if t_fb[1] == '':
    r_fb = Popen(["bash", "script2.sh"])
  time.sleep(1)

