#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qtscrob-%s/src/qt" % get.srcVERSION()

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    pisitools.dobin("qtscrob")

    pisitools.insinto("/usr/share/qtscrobbler/resources", "resources/*")
    pisitools.insinto("/usr/share/qtscrobbler/translations", "translations/*.qm")

    pisitools.dodoc("README", "TODO", "../../AUTHORS", "../../CHANGELOG", "../../COPYING")
