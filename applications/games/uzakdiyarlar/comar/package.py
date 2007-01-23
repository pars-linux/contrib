#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 0777 /usr/share/uzakdiyarlar/log")
    os.system("chmod 0777 /usr/share/uzakdiyarlar/player")
    os.system("chmod 0755 /usr/share/uzakdiyarlar/area/*")