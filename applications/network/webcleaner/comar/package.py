#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/webcleaner-certificates install")
