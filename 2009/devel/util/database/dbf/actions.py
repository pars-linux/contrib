#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "dbf-core"

def setup():
    shelltools.chmod("configure")
    shelltools.chmod("install.sh")

    pisitools.dosed("configure", "docbook-to-man", "docbook2man")
    pisitools.dosed("man/Makefile.in", "docbook-to-man", "docbook2man")

    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make()

    # Fixup man page
    shelltools.move("man/DBF.SECTION","man/dbf.1")

def install():
    autotools.install()

    pisitools.domo("po/tr.po", "tr", "dbf.mo")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "CREDITS", "FAQ", "NEWS", "README")
