#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf()
    autotools.configure("--enable-smtp \
                         --enable-pop \
                         --enable-imap \
                         --enable-imap-edit-threads \
                         --enable-pgp \
                         --enable-nfs-fix \
                         --enable-compressed \
                         --enable-hcache \
                         --enable-smime \
                         --enable-gpgme \
                         --with-curses \
                         --without-gdbm \
                         --with-ssl \
                         --with-bdb \
                         --with-homespool=Maildir \
                         --with-mailpath=/var/spool/mail \
                         --with-docdir=/usr/share/doc/%s"% get.srcTAG())

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/doc/%s/*.html"% get.srcTAG(), "/usr/share/doc/%s/html/"% get.srcTAG())
    pisitools.remove("%s/mime.types"% get.confDIR())
    pisitools.remove("%s/*.dist"% get.confDIR())
    pisitools.remove("/usr/share/doc/%s/INSTALL" % get.srcTAG())
    pisitools.remove("/usr/share/doc/%s/TODO"% get.srcTAG())
