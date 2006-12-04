#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # libtoolize to fix relink bug
    libtools.libtoolize()
    autotools.configure("--enable-nls")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    ###
    #libbonobox.so.2.0.1U libbonobox.so.2 libbonobox.so libbonobox.la 
    pisitools.dolib(".lib/libbonobox.la")
    pisitools.dolib_so(".lib/libbonobox.so.2.0.1U")
    #pisitools.rename("/usr/lib/libbonobox.so.2.0.1U", "libbonobox.so.2.0.1")
    #pisitools.dosym("/usr/lib/libbonobox.so.2.0.1", "/usr/lib/libbonobox.so.2")
    #pisitools.dosym("/usr/lib/libbonobox.so.2.0.1", "/usr/lib/libbonobox.so")
    ###    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")