
#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gtranslator")

def preRemove():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gtranslator")

