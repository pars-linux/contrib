
#!/usr/bin/python

import os

def postInstall():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gtranslator")

def preRemove():
    os.system("scrollkeeper-uninstall -p /var/lib/scrollkeeper /usr/share/omf/gtranslator/gtranslator-C.omf")
