#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/update-desktop-database -q /usr/share/applications")
    os.system("/usr/bin/update-mime-database /usr/share/mime")
