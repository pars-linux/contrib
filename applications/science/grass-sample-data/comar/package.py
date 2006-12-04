#!/usr/bin/python

import os

def postInstall():
    os.system("chmod 777 /opt/grass-6.2.0RC1/samples")