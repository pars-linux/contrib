#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no \
                                  --enable-ipv6 \
                                  --enable-hal \
                                  --with-hal-mount=/usr/bin/mount \
                                  --with-hal-umount=/usr/bin/umount \
                                  --with-hal-eject=/usr/bin/eject")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("TODO", "NEWS", "README", "HACKING", "AUTHORS", "ChangeLog")