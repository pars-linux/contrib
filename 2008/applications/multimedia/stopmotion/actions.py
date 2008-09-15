#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --with-html-dir=--docdir=/usr/share/doc/%s/html" % (get.srcTAG()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "graphics/stopmotion_logo.xpm")

    pisitools.doman("stopmotion.1")
    pisitools.dodoc("AUTHORS", "COPYING", "README")
