#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("src/microcode")
    autotools.configure()

def build():
    shelltools.cd("src/microcode")
    autotools.make()

def install():
    pisitools.dobin("src/microcode/scheme")
    pisitools.dobin("src/microcode/bchscheme")

    pisitools.insinto("/usr/lib", "lib/mit-scheme")

    pisitools.removeDir("/usr/lib/mit-scheme/doc")
    pisitools.removeDir("/usr/lib/mit-scheme/edwin/info")

    pisitools.dohtml("lib/mit-scheme/doc/*.html")
    pisitools.doinfo("lib/mit-scheme/edwin/info/*")
    pisitools.dodoc("lib/mit-scheme/doc/COPYING")
