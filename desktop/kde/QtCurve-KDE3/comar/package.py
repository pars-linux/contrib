#!/usr/bin/python

import os

def postInstall():
    os.system("chmod -R 0777 /usr/kde/3.5/share/apps/qtcurve")