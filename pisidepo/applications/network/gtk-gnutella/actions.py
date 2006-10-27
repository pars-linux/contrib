#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.copy("Configure", "configure")
    autotools.rawConfigure("-d -s -e \
                            -Dprefix=/usr \
                            -Dprivlib=/usr/share/gtk-gnutella \
                            -Dgtkversion=2 \
                            -Dofficial=true \
                            -Ddbus=true \
                            -Dd_enablenls \
                            -Dgmsgfmt=/usr/bin/msgfmt")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","ChangeLog","README","TODO")
