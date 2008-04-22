#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pisitools.remove("%s/usr/lib/python2.4/site-packages/elisa/plugins/__init__.py" %
                     get.installDIR())
    pythonmodules.install()
