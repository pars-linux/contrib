#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pisitools.dosed("images/main.glade", "mini-fluxbox6.png", "../images/mini-fluxbox6.png")
    pisitools.dosed("images/main.glade", "fluxmetal.png", "../images/fluxmetal.png")

    pythonmodules.install()

    pisitools.domove("/usr/share/fluxstyle/docs/", "/usr/share/doc/%s/" % get.srcTAG())
