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
    autotools.configure("--disable-schemas-install \
                        --disable-howl \
			--disable-gnutls \
			--enable-http-neon \
			--enable-openssl \
			--enable-samba \
			--enable-hal \
                        --enable-ipv6 \
			--disable-avahi")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "HACKING", "COPYING*", "INSTALL", "NEWS", "README", "TODO")