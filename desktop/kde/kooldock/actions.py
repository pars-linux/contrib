#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kooldock"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Turkish translation
    pisitools.domo("po/tr.po", "tr", "kooldock.mo")
    pisitools.domove("/usr/share/locale/tr/LC_MESSAGES/kooldock.mo", "%s/share/locale/tr/LC_MESSAGES/" % get.kdeDIR())
    pisitools.removeDir("/usr/share/locale")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
