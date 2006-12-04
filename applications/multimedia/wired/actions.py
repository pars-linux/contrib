#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
#from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
#   autotools.aclocal()
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr")
#   libtools.libtoolize("--copy --force")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    ###Dosya çakışmaları: (20060920)
    #/usr/lib/libportaudio.so.2 from portaudio package
    #/usr/lib/libportaudio.so from portaudio package
    #/usr/lib/libportaudio.la from portaudio package
    #/usr/lib/libportaudio.so.2.0.0 from portaudio package
    #/usr/lib/pkgconfig/portaudio-2.0.pc from portaudio package
    #/usr/lib/libportaudio.a from portaudio package
    pisitools.remove("/usr/lib/libportaudio.so.2")
    pisitools.remove("/usr/lib/libportaudio.so")
    pisitools.remove("/usr/lib/libportaudio.la")
    pisitools.remove("/usr/lib/libportaudio.so.2.0.0")
    pisitools.remove("/usr/lib/pkgconfig/portaudio-2.0.pc")
    pisitools.remove("/usr/lib/libportaudio.a")
    ###
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "BUGS", "INSTALL", "LICENSE", "NEWS", "README", "TODO")
