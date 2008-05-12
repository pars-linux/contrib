#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    autotools.configure("--disable-static \
                         --disable-scrollkeeper \
                         --disable-spell \
                         --enable-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy(lookInto="/usr/lib/gedit-2/plugins")

    pisitools.dodoc("NEWS", "TODO", "README", "BUGS", "AUTHORS", "ChangeLog")
