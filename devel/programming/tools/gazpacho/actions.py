#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()

    pisitools.domove("/usr/share/doc/gazpacho/*","/usr/share/doc/gazpacho-0.7.2-4")
    #gazpacho setup.py automatically installs docs into this folder so removeDir..
    pisitools.removeDir("/usr/share/doc/gazpacho")
    pisitools.dodoc("doc/*")
