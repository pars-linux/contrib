#!/usr/bin/python

import os

def postInstall():
    os.system("gtk-update-icon-cache /usr/share/icons/hicolor")
