#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.automake()
    autotools.configure("--enable-static=no \
                         --enable-hqsinc \
                         --without-sampe-decoders \
                         --with-x \
                         --with-qtdir=%s" % get.qtDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "TODO", "ChangeLog", "NEWS")
