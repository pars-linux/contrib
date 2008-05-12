#!/usr/bin/python

import os

def postInstall():
    os.system("gtk-update-icon-cache -qf /usr/share/icons/hicolor")
