#!/usr/bin/python

import os

def postInstall():
    os.system("update-mime-database /usr/share/mime")