jtouch
======

Simple json-based touch utility

Usage: jtouch [-jd json date time desc] path
<br>
       If desc is present, use date time from there. 
<br>
       Otherwise, use current date time

mvnjars
=======
<br>
<b>Maven support util</b>
<br>
mvnjars -h     - help
<br>
mvnjars -r     - download jars to local directory using mvn dependency:resolve
<br>
mvnjars        - list jars specified in ./pom.xml
<br>
mvnjars -dlib  - copy jars to directory lib 
