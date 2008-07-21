#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    shelltools.system("msgfmt -v po/tr.po -o po/tr.mo")
    pisitools.insinto("%s/share/locale/tr/LC_MESSAGES" % get.kdeDIR(), "po/tr.mo", "subtitlecomposer.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
