#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/xrdp/rsakeys.ini"):
        os.system("/usr/bin/xrdp-keygen xrdp /etc/xrdp/rsakeys.ini")
