#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/scrollkeeper-update -q -p /var/lib/scrollkeeper -o /usr/share/omf")
