#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/build-docbook-catalog")
    
def preRemove():
    os.remove("/etc/xml/docbook")
    os.system("/usr/bin/build-docbook-catalog")    
