#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize()
    autotools.configure("--with-xml-catalog=/etc/xml/catalog \
                         --localstatedir=/var \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/etc/logrotate.d", "scrollkeeper-logrotate")
    pisitools.insinto("/etc/logrotate.d", "scrollkeeper")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO", "scrollkeeper-spec.txt")
