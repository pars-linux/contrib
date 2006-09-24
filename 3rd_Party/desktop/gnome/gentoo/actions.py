#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps", "icons/gentoo.png")
    pisitools.newman("docs/gentoo.1x", "gentoo.1")
    pisitools.dohtml("docs/*.html", "docs/*.css")
    pisitools.dodoc("AUTHORS", "BUGS", "CONFIG-CHANGES", "CREDITS", "ChangeLog", "NEWS", "ONEWS", "README*", "TODO", "docs/FAQ", "docs/menus.txt")
