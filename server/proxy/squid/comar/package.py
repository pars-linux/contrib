#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:squid /usr/lib/squid/ncsa_auth")
    os.system("/usr/bin/chown root:squid /usr/lib/squid/pam_auth")
    os.system("/usr/bin/chown squid:squid /var/log/squid")
    os.system("/usr/bin/chown squid:squid /var/cache/squid")
    os.system("/usr/bin/chmod 4750 /usr/lib/squid/ncsa_auth")
    os.system("/usr/bin/chmod 4750 /usr/lib/squid/pam_auth")
    os.system("/usr/bin/chmod 0755 /var/log/squid")
    os.system("/usr/bin/chmod 0755 /var/cache/squid")
