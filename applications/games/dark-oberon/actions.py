#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "dark-oberon-1.0.2-RC1"

def build():
    autotools.make("SOUND=1")

def install():
    pisitools.insinto("/usr/share/darkoberon", "*")
    pisitools.removeDir("/usr/share/darkoberon/src")
    pisitools.remove("/usr/share/darkoberon/Makefile")
    pisitools.remove("/usr/share/darkoberon/README")