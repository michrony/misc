jtouch
======
<br>
<b>Very simple json-based touch utility</b>
<br>
jtouch path - if ./jtouch.json is present, use date time from there. Otherwise, use current date time
<br>
Example of jtouch.json: {"hm" : [ 13, 15 ], "ymd" : [ 13, 8, 30 ]}

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
