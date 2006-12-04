#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/useradd -d /var/bind -g named -u 40 -s /bin/false named")
    os.system("/usr/bin/chown named:named /var/bind -R")
