#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons

WorkDir="pouetchess_src_0.2.0"

def setup():
    scons.make("configure prefix=/usr datadir=/usr/share/pouetchess")

def build():
    scons.make()

def install():
    pisitools.dobin("bin/pouetChess")
    pisitools.insinto("/usr/share/pouetchess", "data/*")