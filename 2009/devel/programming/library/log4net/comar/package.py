#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/gacutil -i /usr/lib/log4net.dll -check_refs -root /usr/lib/")
