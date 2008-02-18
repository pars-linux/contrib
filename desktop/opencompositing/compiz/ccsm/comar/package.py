#!/usr/bin/python

import os

def postInstall():
    os.system("gtk-update-icon-cache -tf /usr/share/ccsm/icons/hicolor")
