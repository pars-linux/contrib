#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/sbin/groupadd tss")
    os.system("/usr/sbin/useradd -r tss -g tss")
    os.system("/bin/chown tss:tss /etc/tcsd.conf")
    os.system("/bin/chown tss:tss /sbin/tcsd")
    os.system("/usr/bin/mkdir /var/lib/tpm")
    os.system("/usr/bin/chown tss:tss /var/lib/tpm")
    os.system("/bin/chmod 1777 /var/lib/tpm")

def preRemove():
    os.system("/usr/sbin/userdel tss")
    os.system("/usr/sbin/groupdel tss")
    os.system("/usr/bin/rm -Rf /var/lib/tmp/*")
    os.system("/usr/bin/rmdir /var/lib/tmp")