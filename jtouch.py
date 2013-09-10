# jtouch.py

# Simple json-based touch utility
# Usage: jtouch [-jd json date time desc] <path>
#        If desc is present, use date time from there. 
#        Otherwise, use current date time

# Example of desc: 
# {"hm" : [ 13, 15 ], "ymd" : [ 13, 8, 30 ]}

# Version: 07/31/2013
# Version: 08/11/2013: added argparse and -jd option
<<<<<<< HEAD
# Version: 09/10/2013: try using <script dir>/jtouch.json if -jd not specified
=======
>>>>>>> 0fe61343df0b67d1ed8bc957b16892ced808135f

import sys, os, glob, json, time
import argparse
from datetime import datetime

#-------------------------------------------------------------------------
def getCfg(fn):
  if (fn==None):
       print "jtouch: set current date"  
       return ""
       
  if (fn!=None and not os.path.exists(fn)):
       print "jtouch: %s does not exist, set current date" % (fn)  
       return ""
  try:
       cfg = json.loads(open(fn).read())
  except Exception, e:
       print "jtouch: wrong %s, set current date" % (fn)
       return ""
  print "jtouch: use %s %s" % (fn, str(cfg))

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
      print "jtouch: wrong descriptor(%s, %s)" % (str(e), str(cfg))
      exit()

   if (not os.path.exists(fn)): 
      try:    open(fn, 'w').close() 
      except: 
              print "jtouch: wrong file name(%s)" % (fn)
              return
              
   t = time.mktime(t.timetuple())
   os.utime(fn, (t, t))
   print "jtouch: processed(%s)" % (fn)

   return
#-------------------------------------------------------------------------
parser = argparse.ArgumentParser()
<<<<<<< HEAD
parser.add_argument("-jd", type = str, help="json date descriptor. If not specified try using <script dir>/jtouch.json")
parser.add_argument("path", type = str, help="files to process")
args = vars(parser.parse_args())

files     = args["path"]
cfgn      = args["jd"]
scrdircfg = os.path.dirname(sys.argv[0]).replace("\\", "/") + "/jtouch.json"
if (cfgn==None and os.path.exists(scrdircfg)): cfgn = scrdircfg
=======
parser.add_argument("-jd", type = str, help="json date descriptor")
parser.add_argument("path", type = str, help="files to process")
args = vars(parser.parse_args())

files = args["path"]
cfgn  = args["jd"]
>>>>>>> 0fe61343df0b67d1ed8bc957b16892ced808135f
if (cfgn!=None and not cfgn.endswith(".json")): cfgn = cfgn + ".json"
cfg = getCfg(cfgn)

lst = glob.glob(files)
if (len(lst)==0): lst = [files]
for fn in lst: touch(fn, cfg)
