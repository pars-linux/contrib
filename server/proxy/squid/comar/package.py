#!/usr/bin/python

import os
import pwd
import grp

def postInstall():
    try:
        grp.getgrnam("squid")
    except KeyError:
        for gid in range(101,999):
            try:
                grp.getgrgid(gid)
            except KeyError:
                os.system("/usr/sbin/groupadd -g %s squid" % gid)
                break

    try:
        pwd.getpwnam("squid")
    except KeyError:
        for uid in range(101,999):
            try:
                pwd.getpwuid(uid)
            except KeyError:
                os.system("/usr/sbin/useradd -d /var/cache/squid -l -g squid -u %s -s /bin/false squid" % uid)
                break

    os.system("/usr/bin/chown root:squid /usr/lib/squid/ncsa_auth")
    os.system("/usr/bin/chown root:squid /usr/lib/squid/pam_auth")
    os.system("/usr/bin/chown squid:squid /var/log/squid")
    os.system("/usr/bin/chown squid:squid /var/cache/squid")
    os.system("/usr/bin/chmod 4750 /usr/lib/squid/ncsa_auth")
    os.system("/usr/bin/chmod 4750 /usr/lib/squid/pam_auth")
    os.system("/usr/bin/chmod 0755 /var/log/squid")
    os.system("/usr/bin/chmod 0755 /var/cache/squid")
