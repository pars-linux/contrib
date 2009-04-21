#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/etc/freevo")
    pisitools.dodir("/var/cache/freevo")
    pisitools.dodir("/var/log/freevo")

    pythonmodules.install()

    pisitools.insinto("/usr/share/pixmaps", "share/images/logo_david.png", "freevo.png")
    pisitools.insinto("/etc/freevo", "local_conf.py.example", "local_conf.py")
