#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "fmodapi375linux"

def install():
    pisitools.insinto("/usr/include", "api/inc/*")
    pisitools.insinto("/usr/lib", "api/libfmod-3.75.so")
    pisitools.insinto("/usr/share/doc/fmod-3.75-1", "documentation/*")