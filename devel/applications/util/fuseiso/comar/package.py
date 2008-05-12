#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    module = open("/etc/modules.autoload.d/kernel-2.6").read().find("fuse")
    if module == -1:
        os.system("echo fuse >> /etc/modules.autoload.d/kernel-2.6")

    os.system("/sbin/modprobe fuse")
