#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoreconf("-i")
    autotools.aclocal()
    libtools.libtoolize("--copy --force")
    autotools.autoconf()
    autotools.autoheader()
    autotools.automake()

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())
    
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-4.4", "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-4.4", "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-4.4", "docbook.cat")

    pisitools.insinto("/usr/share/sgml/docbook/xml-dtd-4.4/ent", "ent/*.ent")

    pisitools.dodoc("ChangeLog", "README")
