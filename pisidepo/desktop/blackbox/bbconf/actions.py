#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-qt-dir=" + get.qtDIR())

def build():
    autotools.make()

def install():
    autotools.install()
#   pisitools.domove("/usr/doc/bbconf", "/usr/share/doc/%s" % get.srcTAG())
    pisitools.removeDir("/usr/doc")
    pisitools.dodoc("AUTHORS", "LICENSE", "README", "ChangeLog", "COPYING", "INSTALL", "README.html", "TODO")