#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for dirs in ("/etc/teamspeak", "/var/lib/teamspeak", "/var/log/teamspeak", "/var/run/teamspeak"):
        os.system("/bin/chown teamspeak:teamspeak %s" % dirs)
        os.system("/bin/chmod -R 700 %s" % dirs)
