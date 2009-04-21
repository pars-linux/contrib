#!/usr/bin/python

import os

def postInstall():
    os.system("gtk-update-icon-cache -f -t /usr/share/icons/hicolor")
