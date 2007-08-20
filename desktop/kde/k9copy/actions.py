#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Install Turkish translation
    pisitools.domo("po/tr.po" , "tr", "k9copy.mo")
    pisitools.domove("/usr/share/locale/tr/LC_MESSAGES/k9copy.mo", "%s/share/locale/tr/LC_MESSAGES" % get.kdeDIR())
    pisitools.removeDir("/usr/share/locale")

    # Install docs
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
