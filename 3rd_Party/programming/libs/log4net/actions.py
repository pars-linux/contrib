#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def build():
    shelltools.system("sn -k log4net.snk")
    shelltools.system("mcs /t:library /out:bin/log4net.dll -keyfile:log4net.snk /r:System.Data /r:System.Web `find src -name \"*.cs\"`")

def install():
    pisitools.dodir("/usr/lib/log4net")
    pisitools.insinto("/usr/lib/log4net/", "bin/log4net.dll")
    pisitools.dosym("/usr/lib/log4net/log4net.dll", "/usr/web/bin/log4net.dll")
