# orekit_jpype
This repository contains a python installable packaage of stubs for orekit and hipparcus libraries.

They are generated with stubgenj
 
To generate stub files (not working yet), use the stubgenj package 
https://gitlab.cern.ch/scripting-tools/stubgenj

and command line:
python -m stubgenj --convert-strings --no-jpackage-stubs --classpath "../*.jar" org.orekit  org.hipparchus java

Versions..:
baseline
    - Jpype 1.2.1
    - stubgenj 0.2.4
    - openjdk 8 
    


# note that for this the * javadoc.jar files needs to be in that dir.

javadoc for python orekit is generated by:

mvn javadoc:jar -DadditionalJOption=-Xdoclint:none
