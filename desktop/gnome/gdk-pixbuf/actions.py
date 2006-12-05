#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize()
    autotools.configure("--sysconfdir=/etc/X11/gdk-pixbuf")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s sysconfdir=%s/etc/X11/gdk-pixbuf" % (get.installDIR(), get.installDIR()))
    libtools.preplib()

    pisitools.dosed("%s/usr/bin/gdk-pixbuf-config" % get.installDIR(), get.installDIR(), "")
    shelltools.chmod("%s/usr/lib/gdk-pixbuf/loaders", 0755)
    shelltools.chmod("%s/usr/lib/gdk-pixbuf/loaders/*", 0644)

    pisitools.dodoc("AUTHORS", "COPYING*", "README*", "INSTALL", "TODO", "ChangeLog*", "NEWS*")
