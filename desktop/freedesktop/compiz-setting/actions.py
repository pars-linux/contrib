#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
 
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
 
WorkDir = "compiz-settings"
 
def setup():
    shelltools.system("./autogen.sh --prefix=/usr")
    autotools.configure()
 
def build():
    autotools.make()
 
def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR()) 
