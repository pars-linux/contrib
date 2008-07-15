#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="figlet222"

def build():
    autotools.make("DEFAULTFONTDIR=/usr/share/figlet/fonts")

def install():
    pisitools.dobin("figlet")
    pisitools.dobin("figlist")
    pisitools.dobin("showfigfonts")

    pisitools.insinto("/usr/share/figlet/fonts", "fonts/*")
