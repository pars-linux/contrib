#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "drpython"
drpython_dir = "/usr/lib/%s/site-packages/drpython" % get.curPYTHON()

def setup():
    pisitools.dosed("drpython.lin", r"\${0\%/\*}", drpython_dir)

def install():
    pythonmodules.install()

    pisitools.dosym("%s/drpython.lin" % drpython_dir, "/usr/bin/drpython")
    pisitools.dosym("%s/bitmaps/drpython.png" % drpython_dir, "/usr/share/pixmaps/drpython.png")

    shelltools.chmod("%s%s/drpython.lin" % (get.installDIR(), drpython_dir))

    pisitools.dodoc("*.txt")

    pisitools.remove("/usr/bin/postinst.py")
    pisitools.remove("%s/postinst.py" % drpython_dir)
