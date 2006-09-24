#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #shelltools.system("/usr/bin/sed -i -e \"s:GST.*LOCK://\\0:\" ext/jpeg2000/gstj2kdec.c")
    #no configure   
    #shelltools.system("./autogen.sh")
    pisitools.dosed("ext/jpeg2000/gstj2kdec.c", "GST_LOCK (pad);", "//GST_LOCK (pad);")
    pisitools.dosed("ext/jpeg2000/gstj2kdec.c", "GST_UNLOCK (pad);", "//GST_UNLOCK (pad);")
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-jingle-p2p \
                         --enable-jasper  \
                         --disable-debug \
                         --with-plugins=rtpdemux,rtpjitterbuffer")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")