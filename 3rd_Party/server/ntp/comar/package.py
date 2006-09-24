#!/usr/bin/python

import os
import pwd
import grp

def postInstall():
    try:
        grp.getgrnam("ntp")
    except KeyError:
        for gid in range(101,999):
            try:
                grp.getgrgid(gid)
            except KeyError:
                os.system("/usr/sbin/groupadd -g %s ntp" % gid)
                break

    try:
        pwd.getpwnam("ntp")
    except KeyError:
        for uid in range(101,999):
            try:
                pwd.getpwuid(uid)
            except KeyError:
                os.system("/usr/sbin/useradd -d /dev/null -g ntp -u %s -s /bin/false ntp" % uid)
                break

    os.system("/usr/bin/chown ntp:ntp /var/lib/ntp")
