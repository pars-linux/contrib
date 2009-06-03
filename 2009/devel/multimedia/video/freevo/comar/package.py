#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/chmod 1777 /var/cache/freevo")
    os.system("/usr/bin/chmod 1777 /var/log/freevo")
    os.system("freevo setup")