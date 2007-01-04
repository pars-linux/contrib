#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "freevo-1.7.0-rc2"

def install():
    pisitools.dodir("/etc/freevo")
    pisitools.dodir("/var/cache/freevo")
    pisitools.dodir("/var/log/freevo")

    pythonmodules.install()

    pisitools.insinto("/usr/share/pixmaps", "share/images/logo_david.png", "freevo.png")
    pisitools.insinto("/etc/freevo", "local_conf.py.example", "local_conf.py")
