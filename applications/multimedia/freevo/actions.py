#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="freevo-1.6.0"

def install():
    pisitools.dodir("/etc/freevo")
    pisitools.dodir("/var/cache/freevo")
    pisitools.dodir("/var/log/freevo")
    pythonmodules.install()
    pisitools.insinto("/etc/freevo", "local_conf.py.example")
    pisitools.rename("/etc/freevo/local_conf.py.example", "local_conf.py")
