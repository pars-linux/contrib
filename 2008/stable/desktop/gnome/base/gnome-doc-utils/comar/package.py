#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-make")
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-xslt")

def preRemove():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-make")
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-xslt")
