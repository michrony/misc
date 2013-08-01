jtouch
======

Very simple json-based touch utility

jtouch path - if ./jtouch.json is present, use date time from there. Otherwise, use current date time

Example of jtouch.json: {"hm" : [ 13, 15 ], "ymd" : [ 13, 8, 30 ]}

mvnjars
=======

Maven support util

mvnjars -h     - help

mvnjars -r     - download jars to local directory using mvn dependency:resolve

mvnjars        - list jars specified in ./pom.xml

mvnjars -dlib  - copy jars to directory lib 
