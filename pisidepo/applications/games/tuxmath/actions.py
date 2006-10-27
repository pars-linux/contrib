#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="tuxmath"

def setup():
    pass

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/tuxmax")
    pisitools.dodir("/usr/bin")
    autotools.install()
    pisitools.dodoc("docs/*.txt")

