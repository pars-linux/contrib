#!/usr/bin/python

import os

def postInstall():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gedit")

def preRemove():
    PATH = "/usr/share/omf/gedit"

    for root, dirs, files in os.walk(PATH):
        for file in files:
            os.system("scrollkeeper-uninstall -p /var/lib/scrollkeeper %s/%s" % (PATH, file))
