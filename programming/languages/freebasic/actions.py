#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "FreeBASIC"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/usr/share")
    shelltools.system("./install.sh -i %s/usr/share" % get.installDIR())
    pisitools.dosym("/usr/share/freebasic/fbc", "/usr/bin/fbc")
    pisitools.dodoc("changelog.txt", "migrating.txt", "readme.txt", "docs/*")