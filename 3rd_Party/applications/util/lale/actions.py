#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/lale", "*.lal")
    pisitools.doexe("lale", "/usr/share/lale/")
    pisitools.dodoc("*.txt")
    shelltools.chmod("%s/usr/share/lale/lale" % get.installDIR(), 0755)