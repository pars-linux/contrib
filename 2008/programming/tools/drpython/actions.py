#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "drpython"
drpython_dir = "/usr/lib/%s/site-packages/drpython" % get.curPYTHON()

def fixfiles(d):
    import os
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name == ".cvsignore":
                try:
                    os.unlink(os.path.join(root,name))
                except:
                    pass

def setup():
    fixfiles(".")
    pisitools.dosed("drpython.lin", r"\${0\%/\*}", drpython_dir)

def install():
    pythonmodules.install()

    pisitools.rename("/usr/bin/drpython.lin", "drpython")
    pisitools.dosym("%s/bitmaps/drpython.png" % drpython_dir, "/usr/share/pixmaps/drpython.png")

    pisitools.dodoc("*.txt")
