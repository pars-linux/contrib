#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libnasl"

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure()
                        
def build():
    autotools.make("-C nasl cflags")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
