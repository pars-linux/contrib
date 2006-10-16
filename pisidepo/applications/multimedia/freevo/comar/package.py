#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 777 /var/cache/freevo")
    os.system("chmod 777 /var/log/freevo")
    os.system("freevo setup")