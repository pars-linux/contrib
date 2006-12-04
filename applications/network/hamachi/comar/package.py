#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/modprobe tun")
    os.system("tuncfg")

def preRemove():
    os.system("/sbin/modprobe -r tun")