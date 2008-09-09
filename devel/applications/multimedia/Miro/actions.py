#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    shelltools.cd("platform/gtk-x11")
    pythonmodules.compile()

def install():
    shelltools.cd("platform/gtk-x11")
    pythonmodules.install()
