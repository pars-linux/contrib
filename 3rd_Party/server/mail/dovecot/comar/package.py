#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/groupadd -g 97 dovecot")
    os.system("/usr/sbin/useradd -d /usr/libexec/dovecot -g dovecot -u 97 -s /sbin/nologin dovecot")

    os.system("/usr/bin/chown root:0 /var/run/dovecot")
    os.system("/usr/bin/chown root:dovecot /var/run/dovecot/login")
    os.system("/usr/bin/chmod 0700 /var/run/dovecot")
    os.system("/usr/bin/chmod 0750 /var/run/dovecot/login")
    os.system("/usr/bin/chmod 0600 /etc/dovecot.conf")
