#!/usr/bin/python

import os

def postInstall():
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-make")
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnome-doc-xslt")

def preRemove():
    os.system("scrollkeeper-uninstall -p /var/lib/scrollkeeper /usr/share/omf/gnome-doc-make/gnome-doc-make-C.omf")
    os.system("scrollkeeper-uninstall -p /var/lib/scrollkeeper /usr/share/omf/gnome-doc-xslt/gnome-doc-xslt-C.omf")
