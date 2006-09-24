#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--localstatedir=/var \
                         --with-mysql \
                         --with-pgsql \
                         --with-ssl=openssl \
                         --with-ssldir=/etc/ssl \
                         --with-pam \
                         --with-ldap")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/doc/dovecot")
    pisitools.rename("/etc/dovecot-example.conf", "dovecot.conf")
    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO", "dovecot-example.conf")
    pisitools.dodoc("doc/*.txt", "doc/*.conf", "doc/*.cnf", "doc/mkcert.sh")
    pisitools.dodir("/var/run/dovecot")
    pisitools.dodir("/var/run/dovecot/login")
