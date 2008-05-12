#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("gtk-update-icon-cache -f -t /usr/share/icons/hicolor")
