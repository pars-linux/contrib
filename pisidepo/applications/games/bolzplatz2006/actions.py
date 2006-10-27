#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    pass

def build():
    pass

def install():
    shelltools.system("tar xzvf bp2k6-linux.tar.gz && tar xvf bp2k6-startscript.gz")
    pisitools.dosed("bp2k6", "/usr/share/games/bolzplatz2006", "/usr/share/bolzplatz2006")
    pisitools.dobin("bp2k6")
    pisitools.insinto("/usr/share/bolzplatz2006", "bolzplatz2006/*")