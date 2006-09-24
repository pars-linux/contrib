#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "XGngeo-16_beta"

def setup():
    pass

def build():
    pass

def install():
    pythonmodules.install()
    
    pisitools.dosym("/usr/share/xgngeo/img/xgngeo.png", "/usr/share/pixmaps/xgngeo.png")
    pisitools.domove("/usr/bin/xgngeo_startup.py", "/usr/bin", "xgngeo")
    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "PKG-INFO", "README.txt", "doc/*")
