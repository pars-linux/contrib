#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 0755 /usr/share/trigger/trigger.config.defs")