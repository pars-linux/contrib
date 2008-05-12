#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="mysqlcc-%s-src" % get.srcVERSION()

def setup():
    autotools.configure("--with-qt=/usr/qt/3")

def build():
    autotools.make()

def install():
    pisitools.dobin("mysqlcc")
    pisitools.insinto("/usr/share/mysqlcc", "*.wav")
    pisitools.insinto("/usr/share/mysqlcc", "syntax.txt")
    pisitools.insinto("/usr/share/pixmaps", "mysqlcc.xpm")
    pisitools.insinto("/usr/share/mysqlcc/translations", "translations/*")

    pisitools.dodoc("Changelog.txt")

