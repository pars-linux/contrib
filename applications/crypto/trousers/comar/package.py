#!/usr/bin/python

import os

def postInstall():
    os.system("/bin/chown tss:tss /etc/tcsd.conf")
    os.system("/bin/chown tss:tss /usr/sbin/tcsd")
    os.system("/usr/bin/mkdir /var/lib/tpm")
    os.system("/usr/bin/chown tss:tss /var/lib/tpm")
    os.system("/bin/chmod 1777 /var/lib/tpm")

def preRemove():
    os.system("/usr/bin/rm -Rf /var/lib/tmp/*")
    os.system("/usr/bin/rmdir /var/lib/tmp")
