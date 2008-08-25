#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--prefix=/usr/share/grisbi")
    pisitools.dosed("src/Makefile", "/doc/grisbi", "/doc/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dosym("/usr/share/pixmaps/grisbi/grisbi.png", "/usr/share/pixmaps/grisbi.png")
    pisitools.domove("/usr/share/doc/grisbi/help", "%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "OLDNEWS", "README")
