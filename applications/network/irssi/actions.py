#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-ssl \
                         --disable-glibtest \
                         --with-socks \
                         --with-textui \
                         --with-bot \
                         --with-proxy \
                         --with-terminfo \
                         --with-modules \
                         --without-perl-staticlib")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.rename("/usr/bin/irssi", "irssi-bin")
