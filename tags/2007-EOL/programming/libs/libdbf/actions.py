#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libdbf"

def setup():
    shelltools.chmod("configure")
    shelltools.chmod("install-sh")
    pisitools.dosed("configure","docbook-to-man","docbook2man")

    autotools.rawConfigure("--prefix=/usr \
                            --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domo("po/tr.po", "tr", "libdbf.mo")

    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(),"man/html")
    pisitools.dodoc("ChangeLog", "COPYING", "README")
