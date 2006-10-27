#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    scons.make()

def install():
    scons.install()
    pisitools.domove("/bin", "/usr/")
    pisitools.domove("/share", "/usr/")
    pisitools.dodoc("doc/*")