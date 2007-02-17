#!/usr/bin/python

import os

def postInstall():
    os.system("gtk-update-icon-cache -f -t /usr/share/icons/hicolor")
    os.system("scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/gnomebaker")

def preRemove():
    os.system("scrollkeeper-uninstall -p /var/lib/scrollkeeper /usr/share/omf/gnomebaker/gnomebaker-C.omf")
