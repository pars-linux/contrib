#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tuxmath"

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/tuxmath")
    pisitools.dodir("/usr/bin")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("docs/*.txt")

    pisitools.removeDir("/usr/share/tuxmath/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/cities/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/tux/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/status/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/status/.xvpics")
    pisitools.removeDir("/usr/share/tuxmath/images/ufos/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/backgrounds/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/backgrounds/CVS/CVS")
    pisitools.removeDir("/usr/share/tuxmath/images/comets/CVS")
    pisitools.removeDir("/usr/share/tuxmath/sounds/CVS")


