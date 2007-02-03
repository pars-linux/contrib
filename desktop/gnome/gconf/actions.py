#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "GConf-2.16.0"

def setup():
    autotools.configure("--enable-gtk")
    
    
def build():
    autotools.make()


def install():
    autotools.install()
    
    ## hack hack
    pisitools.dodir("/etc/gconf/gconf.xml.mandatory")
    pisitools.dodir("/etc/gconf/gconf.xml.defaults")
    shelltools.touch("%s/etc/gconf/gconf.xml.mandatory/.keep3" % get.installDIR())
    shelltools.touch("%s/etc/gconf/gconf.xml.defaults/.keep3" % get.installDIR())

    pisitools.dodir("/etc/env.d")
    pisitools.dodir("/root/.gconfd")
    ##
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")