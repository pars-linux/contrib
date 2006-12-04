#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "sancho-0.9.4-57-linux-gtk"

def install():
    pisitools.dobin("sancho-bin")
    pisitools.dodoc("distrib/*.txt", "AUTHORS", "README")
    pisitools.insinto("/usr/share/sancho", "distrib/*")
    pisitools.insinto("/usr/lib", "lib/*")
    pisitools.insinto("/usr/share/pixmaps/", "distrib/sancho-32.xpm",  "sancho.xpm")

    #File conflict:
    #/usr/lib/libiconv.so from sancho package dependency with libiconv
    pisitools.remove("/usr/lib/libiconv.so*")