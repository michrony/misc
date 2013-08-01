# jtouch.py

# Very simple json-based touch utility
# Usage: jtouch <path>
#        If ./jtouch.json is present, use date ime from there. 
#        Otherwise, use current date time

# Example of jtouch.json: 
# {"hm" : [ 13, 15 ], "ymd" : [ 13, 8, 30 ]}

# Version: 07/31/2013

import sys, os, glob, json, time
from datetime import datetime

#-------------------------------------------------------------------------
def getCfg(fn):
  try:
       cfg = json.loads(open(fn).read())
  except Exception, e:
       print "jtouch: set current date"
       return ""
  print "jtouch: use %s" % (str(cfg))

  return cfg
#-------------------------------------------------------------------------
def touch(fn, cfg):
   t = datetime.now()
 
   if (cfg!=""): 
     try:
      y = int(cfg["ymd"][0])
      m  = int(cfg["ymd"][1])
      d  = int(cfg["ymd"][2])
      h  = int(cfg["hm"][0])
      mi = int(cfg["hm"][1])
      t = datetime(y, m, d, h, mi)
     except Exception, e:
      print "jtouch: wrong jtouch.json - %s" % (str(e))
      exit()

   if (not os.path.exists(fn)): open(fn, 'w').close() 
   t = time.mktime(t.timetuple())
   os.utime(fn, (t, t))
   print "jtouch: set date to %s" % (fn)

   return
#-------------------------------------------------------------------------
if (len(sys.argv)>1): 
   lst = glob.glob(sys.argv[1])
   if (len(lst)==0): lst = [sys.argv[1]]
   cfg = getCfg("./jtouch.json")
   for fn in lst: touch(fn, cfg)
else: print "jtouch: wrong call"
