# mvnjars - copy dependency jars specified in ./pom.xml to the specified directory
# Note: calls maven mvn

# Version: 12/19/2012
# Version: 12/26/2012 - added jars download to mvn repository

help = '''
List/copy dependency jars specified by ./pom.xml
mvnjars -h     - help
mvnjars -r     - download jars to local repository by mvn dependency:resolve
mvnjars        - list jars specified in ./pom.xml
mvnjars -dlib  - copy jars to lib
'''

import os, sys, shutil

dirOut = ""
resolve = False
for el in sys.argv:
 if (el=="-h"):
    print help
    exit()
 if (el.find("-d")==0): dirOut  = el[2:]   
 if (el.find("-r")==0): resolve = True   

if (not os.path.exists("./pom.xml")):
    print "No pom.xml found"
    exit()

print "mvnjars start"

if (resolve):
    ResOK = False
    Res = os.popen("mvn dependency:resolve").readlines()
    for el in Res: 
        if (el.find("BUILD SUCCESSFUL")>0): ResOK = True
    print "mvnjars dependency:resolve: %s" % ResOK

if (not os.path.isdir(dirOut)): dirOut = ""
print "Output directory: %s" % dirOut

Cmd = "mvn dependency:build-classpath"
CmdOut = os.popen(Cmd).readlines()
Res = ""
for line in CmdOut:
  if (line.find(".jar")>0): 
     line = line.replace("\n", "")
     Res = line.split(";")
     break
lRes = len(Res)
print "jars found: %d" % lRes
if (lRes==0):
    print "mvnjars stop"
    exit()

# List files if no copy requested
if (dirOut==""):
   for file in Res:
       file = file.replace("\\", "/")
       file = file.split("/")
       file = file[len(file)-1]
       print file
   print "mvnjars stop"
   exit()

for file in Res:
    shutil.copy2(file, dirOut)
    print "copied: %s" % file

print "mvnjars stop"
