#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown named:named /var/bind -R")
